from django.shortcuts import render
from rest_framework import permissions, viewsets
from .models import Rating, Review
from .serializers import RatingSerializer, ReviewSerializer
from .permissions import IsOwnerOrReadOnly

# Create your views here.
class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [permissions.IsAuthenticated(), IsOwnerOrReadOnly()]
        return [permissions.AllowAny()]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)



class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [permissions.IsAuthenticated(), IsOwnerOrReadOnly()]
        return [permissions.AllowAny()]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)