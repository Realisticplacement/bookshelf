from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager 
# Create your models here.
class UserManager (BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        if not email :
            raise ValueError('The Email field must be set')
        if not username :
            raise ValueError('The Username field must be set')
        
        email = self.normalize_email(email)
        user = self.model(email= email, username= username, **extra_fields)
        user.set_password(password)
        user.save(using= self._db)

        return user
    

    def create_superuser(self, email, username, password= None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_superuser(email, username, password, **extra_fields)
    

class User(AbstractUser):

    email = models.CharField(unique=True)
    username = models.CharField(max_length= 150, unique=True)
    ROLE_CHOICE = (('reader', 'Reader'), ('libarian','Libarian'))
    role = models.CharField(max_length=20, choices=ROLE_CHOICE, default='reader')
    profile_picture = models.ImageField(upload_to='profile_pictures', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

        
