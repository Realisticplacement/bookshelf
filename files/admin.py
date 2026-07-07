from django.contrib import admin
from .models import BookFile, DownloadHistory

# Register your models here.
admin.site.register(BookFile)
admin.site.register(DownloadHistory)