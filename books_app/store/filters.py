import django_filters

from store.models import Book


class BookFilter(django_filters.FilterSet):
    # price = django_filters.NumberFilter()
    class Meta:
        model = Book
        fields = (
            'price',
        )
