from django.urls import path, include
from rest_framework.routers import DefaultRouter
from reviews.views import ReviewViewSet, RatingViewSet


router = DefaultRouter()
router.register(r'ratings', RatingViewSet, basename='rating')
router.register(r'reviews', ReviewViewSet, basename='review')

urlpatterns = [
    path('', include(router.urls)),
]