from django.db import models
from books.models import Book
from accounts.models import User

# Create your models here.
class Rating(models.Model):
    book = models.ForeignKey('books.Book', on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name='ratings')
    rating = models.PositiveSmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('book', 'user')

    def __str__(self):
        return f'Rating {self.rating} for {self.book.title} by {self.user.username}'
    


class Review(models.Model):
    book = models.ForeignKey('books.Book', on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name='reviews')
    rating = models.OneToOneField(Rating, on_delete=models.CASCADE, related_name='review')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('book', 'user')

    def __str__(self):
        return f'Review for {self.book.title} by {self.user.username}'