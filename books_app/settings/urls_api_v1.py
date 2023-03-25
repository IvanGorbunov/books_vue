from django.urls import path, include


urlpatterns = [
    path('', include('store.urls_api_v1')),
]
