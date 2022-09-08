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

    def number_of_story_starts(self):
        pass


class StoryMiddle(models.Model):
    story_text = models.CharField(max_length=50, unique=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE)

    class Meta:
        ordering = ['creation_date']

    def __str__(self):
        return self.story_text

    def number_of_story_middles(self):
        pass


class StoryEnd(models.Model):
    story_text = models.CharField(max_length=60, unique=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE)

    class Meta:
        ordering = ['creation_date']

    def __str__(self):
        return self.story_text

    def number_of_story_ends(self):
        pass


class StoryIdeas(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    story_text = models.CharField(max_length=200)
    creation_date = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.title
    
    def number_of_story_ideas(self):
        pass
