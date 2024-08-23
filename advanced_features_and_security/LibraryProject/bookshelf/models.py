from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    publication_year = models.PositiveIntegerField(default=2000)  # Set default value
    isbn = models.CharField(max_length=13, unique=True)
    pages = models.PositiveIntegerField()
    cover = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)

    def __str__(self):
        return self.username
