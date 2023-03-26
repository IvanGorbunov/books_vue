import django_filters

from store.models import Book


class BookFilter(django_filters.FilterSet):
    class Meta:
        model = Book
        fields = (
            'price',
        )
