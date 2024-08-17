from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    download_link = models.URLField(blank=True)
    cover_image = models.ImageField(upload_to='book_covers/', blank=True, null=True)  # Field for book cover image
    
    
