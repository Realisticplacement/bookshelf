from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=255)
    bio = models.TextField(blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)

    def __str__(self):
        return self.name
    

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)

    def __str__(self):
        return self.name
    


class Tag(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True, null=True)

    def __str__(self):
        return self.name
    

class Series(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True, null=True)

    def __str__(self):
        return self.name




class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='books')
    tags = models.ManyToManyField(Tag, blank=True)
    series = models.ForeignKey('Series', on_delete=models.SET_NULL, blank=True, null=True, related_name='books')
    description = models.TextField()
    summary = models.TextField(blank=True, null=True)
    published_date = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)
    cover_image = models.ImageField(upload_to='book_covers', blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)

    def __str__(self):
        return self.title
