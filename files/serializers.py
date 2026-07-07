from rest_framework import serializers
from .models import BookFile, DownloadHistory


class BookFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookFile
        fields = ['id', 'file', 'book', 'format']

class DownloadHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = DownloadHistory
        fields = ['id', 'user', 'book_file', 'download_count', 'downloaded_at']