import django_filters

from store.models import Book


class BookFilter(django_filters.FilterSet):
    search_fields = (
        'name',
        'author_name',
    )

    class Meta:
        model = Book
        fields = (
            'price',
        )
