from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class Genre(models.Model):
    genre_title = models.CharField(max_length=20, unique=True)
    genre_image = CloudinaryField('image', default='placeholder')
    creation_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['creation_date']

    def __str__(self):
        return self.genre_title
