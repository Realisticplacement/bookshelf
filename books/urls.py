from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AuthorViewSet, BookViewSet, TagViewSet, CategoryViewSet, SeriesViewSet

router = DefaultRouter()
router.register(r'authors', AuthorViewSet, basename='author')
router.register(r'books', BookViewSet, basename='book')
router.register(r'tags', TagViewSet, basename='tag')
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'series', SeriesViewSet, basename='series')

urlpatterns = [
    path('', include(router.urls)),
]