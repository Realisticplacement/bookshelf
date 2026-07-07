from rest_framework import serializers
from .models import BookFile, DownloadHistory


class BookFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookFile
        fields = ['id', 'file', 'book', 'format', 'download_count']

class DownloadHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = DownloadHistory
        fields = ['id', 'user', 'book_file', 'downloaded_at']