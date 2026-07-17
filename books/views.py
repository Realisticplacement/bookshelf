from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Author, Series, Tag, Category, Book
from .serializers import AuthorSerializer, SeriesSerializer, TagSerializer, CategorySerializer, BookSerializer
from .permissions import IsAdminOrReadOnly, IsBookManagerOrReadOnly

# Create your views here.



class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAdminOrReadOnly]



class SeriesViewSet(viewsets.ModelViewSet):
    queryset = Series.objects.all()
    serializer_class = SeriesSerializer
    permission_classes = [IsAdminOrReadOnly]



class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAdminOrReadOnly]



class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]



class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsBookManagerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(uploaded_by=self.request.user)

    def get_queryset(self):
      
      queryset = Book.objects.all()
      queryset = queryset.select_related('author', 'series', 'category')
      queryset = queryset.prefetch_related('tags')
      category_id = self.request.query_params.get('category_id')
      if category_id:
        queryset = queryset.filter(category_id=category_id)

      return queryset
