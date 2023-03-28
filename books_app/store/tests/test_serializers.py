from django.test import TestCase

from store.serializers import BooksSerializer
from store.tests.factories import BookFactory


class BooksSerializerTestCase(TestCase):
    def test_ok(self):
        book_1 = BookFactory(name='Test book 1', price=25, author_name='Author 1')
        book_2 = BookFactory(name='Test book 2', price=55, author_name='Author 1')
        data = BooksSerializer([book_1, book_2], many=True).data
        expected_data = [
            {
                'id': book_1.id,
                'name': 'Test book 1',
                'price': '25.00',
                'author_name': 'Author 1'
            },
            {
                'id': book_2.id,
                'name': 'Test book 2',
                'price': '55.00',
                'author_name': 'Author 1'
            },
        ]
        self.assertEqual(expected_data, data)

