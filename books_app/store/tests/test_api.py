from rest_framework import status
from rest_framework.reverse import reverse_lazy
from rest_framework.test import APITestCase

from store.models import Book
from store.serializers import BooksSerializer
from store.tests.factories import BookFactory


class LogicTestCase(APITestCase):

    def setUp(self):
        self.book_1 = BookFactory(name='Book 1', price=25, author_name='Author 1')
        self.book_2 = BookFactory(name='Book 2', price=55, author_name='Author 5')
        self.book_3 = BookFactory(name='Book Author 1', price=55, author_name='Author 2')

    def test_list_01_url_exists_at_desired_location(self):
        response = self.client.get('/api/v1/book/')
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_list_02_url_accessible_by_name(self):
        response = self.client.get(reverse_lazy('store:book-list'))
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_list_03_get(self):
        books = Book.objects.all()
        serializer_data = BooksSerializer(books, many=True).data
        response = self.client.get(reverse_lazy('store:book-list'))
        self.assertEqual(status.HTTP_200_OK, response.status_code)

        self.assertEqual(serializer_data, response.data)

    def test_list_04_filter(self):
        serializer_data = BooksSerializer([self.book_2, self.book_3], many=True).data
        response = self.client.get(reverse_lazy('store:book-list'), data={'price': '55.00'})
        self.assertEqual(status.HTTP_200_OK, response.status_code)

        self.assertEqual(serializer_data, response.data)

    def test_list_05_search(self):
        serializer_data = BooksSerializer([self.book_1, self.book_3], many=True).data
        response = self.client.get(reverse_lazy('store:book-list'), data={'search': 'Author 1'})
        self.assertEqual(status.HTTP_200_OK, response.status_code)

        self.assertEqual(serializer_data, response.data)

    def test_list_06_ordering(self):
        books = Book.objects.order_by('-price').all()
        serializer_data = BooksSerializer(books, many=True).data
        response = self.client.get(reverse_lazy('store:book-list'), data={'ordering': '-price'})
        self.assertEqual(status.HTTP_200_OK, response.status_code)

        self.assertEqual(serializer_data, response.data)
