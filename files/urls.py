from django.urls import path, include
from rest_framework import routers
from .views import BookFileViewSet, DownloadHistoryViewSet

router = routers.DefaultRouter()
router.register(r'book-files', BookFileViewSet, basename='bookfile')
router.register(r'download-history', DownloadHistoryViewSet, basename='downloadhistory')

urlpatterns = [
    path('', include(router.urls)),
]