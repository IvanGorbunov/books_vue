from django.urls import path, include
from rest_framework.routers import SimpleRouter

from . import views

app_name = 'store'

router = SimpleRouter()
router.register(r'book', views.BooksViewSet)

urlpatterns = [
    path('books-list/', views.BooksListViewSet.as_view(), name='list'),
]
urlpatterns += router.urls
