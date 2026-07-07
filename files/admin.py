from django.contrib import admin
from .models import BookFile, DownloadHistory

# Register your models here.
admin.site.register(BookFile)
class BookFileAdmin(admin.ModelAdmin):
    list_display = ("Book", "download_count")
admin.site.register(DownloadHistory)