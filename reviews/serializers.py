from rest_framework import serializers
from .models import Rating, Review


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['id', 'book', 'user', 'rating', 'created_at', 'updated_at']

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'book', 'user', 'content', 'created_at', 'updated_at']