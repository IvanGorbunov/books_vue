from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet

from store.filters import BookFilter
from store.models import Book
from store.serializers import BooksSerializer


class BooksViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BooksSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter,)
    filterset_class = BookFilter
    search_fields = (
        'name',
        'author_name',
    )


class BooksListViewSet(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BooksSerializer
    filterset_class = BookFilter
    filter_backends = (DjangoFilterBackend, SearchFilter,)
    search_fields = (
        'name',
        'author_name',
    )

