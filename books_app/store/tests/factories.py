import string

from factory import fuzzy
from factory.django import DjangoModelFactory

from store.models import Book


class BookFactory(DjangoModelFactory):
    """
    Фабрика книги
    """
    name = fuzzy.FuzzyText(length=255)
    price = fuzzy.FuzzyDecimal(low=1, high=100000)

    class Meta:
        model = Book



