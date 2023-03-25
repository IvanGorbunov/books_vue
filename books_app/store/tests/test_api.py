from rest_framework import status
from rest_framework.reverse import reverse_lazy
from rest_framework.test import APITestCase

from store.models import Book
from store.serializers import BooksSerializer
from store.tests.factories import BookFactory


class LogicTestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        number_of_items = 33
        for client_id in range(number_of_items):
            BookFactory(name='Book ' + str(client_id))

    def test_list_01_url_exists_at_desired_location(self):
        response = self.client.get('/api/v1/book/')
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_list_02_url_accessible_by_name(self):
        response = self.client.get(reverse_lazy('store:book-list'))
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_get(self):
        books = Book.objects.all()
        response = self.client.get(reverse_lazy('store:book-list'))
        serializer_data = BooksSerializer(books, many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)
