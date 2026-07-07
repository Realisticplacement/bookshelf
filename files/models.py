from django.db import models
from books.models import Book
from accounts.models import User

# Create your models here.

class BookFile(models.Model):
    class Format(models.TextChoices):
        PDF = 'pdf', 'PDF'
        EPUB = 'epub', 'EPUB'

    file = models.FileField(upload_to= 'bookfiles/')
    book = models.ForeignKey(Book, on_delete= models.CASCADE, related_name= 'files')
    format = models.CharField(max_length=10, choices=Format.choices)
    download_count = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = ('book', 'format')

        def __str__ (self):
            return f'{self.book.title} ({self.format})'
        

class DownloadHistory(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE, related_name= 'download_history')
    book_file = models.ForeignKey(BookFile, on_delete= models.CASCADE, related_name= 'download_history')
    downloaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Downloaded {self.book_file} at {self.downloaded_at}'
    