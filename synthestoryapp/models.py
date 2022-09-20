from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Genre(models.Model):
    genre_title = models.CharField(max_length=20, unique=True)
    genre_image = CloudinaryField('image', default='placeholder')
    genre_description = models.CharField(max_length=200)
    creation_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['creation_date']

    def __str__(self):
        return self.genre_title


class StoryStart(models.Model):
    story_text = models.CharField(max_length=30, unique=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE)

    class Meta:
        ordering = ['creation_date']

    def __str__(self):
        return self.story_text


class StoryMiddle(models.Model):
    story_text = models.CharField(max_length=50, unique=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE)

    class Meta:
        ordering = ['creation_date']

    def __str__(self):
        return self.story_text

class StoryEnd(models.Model):
    story_text = models.CharField(max_length=60, unique=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE)

    class Meta:
        ordering = ['creation_date']

    def __str__(self):
        return self.story_text


class StoryIdea(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=30, blank=False)
    story_text = models.CharField(max_length=200, blank=False)
    creation_date = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated_on']

    def __str__(self):
        return self.title
