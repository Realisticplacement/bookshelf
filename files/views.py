from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from django.http import FileResponse

from books.permissions import IsAdminOrReadOnly
from .models import BookFile #, DownloadHistory
from .serializers import BookFileSerializer#, DownloadHistorySerializer


# Create your views here.
class BookFileViewSet(viewsets.ModelViewSet):
    queryset = BookFile.objects.all()
    serializer_class = BookFileSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['get'], permission_classes=[IsAuthenticated])
    def download(self, request, pk=None):
        book_file = self.get_object()
        user = request.user
        response = FileResponse(book_file.file, content_type= 'application/octet-stream')
        response['Content-Disposition'] = f'attachment; filename="{book_file.file.name}"'
        return response



#class DownloadHistoryViewSet(viewsets.ModelViewSet):
    #queryset = DownloadHistory.objects.all()
   # serializer_class = DownloadHistorySerializer
   # permission_classes = [IsAdminOrReadOnly]