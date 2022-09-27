"""
Code for the classes which act as
models in Django
"""
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Genre(models.Model):
    """
    Class for the Genre Model.
    Genre has a genre_title attribute representing a title.
    Genre has a genre_image attribute representing an image of the genre.
    Genre has a genre_description attribute describing the genre.
    Genre has a creation_date attribute which is represented by DateTime.
    """
    genre_title = models.CharField(max_length=20, unique=True)
    genre_image = CloudinaryField('image', default='placeholder')
    genre_description = models.CharField(max_length=200)
    creation_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        """
        Orders the data of the Genre model so that
        it goes by creation date, with the earliest coming
        first.
        """
        ordering = ['creation_date']

    def __str__(self):
        return str(self.genre_title)


class StoryStart(models.Model):
    """
    Class for the StoryStart Model.
    StoryStart has a story_text attribute representing the
    start of a story idea.
    StoryStart has a creation_date which is represented
    by DateTime.
    StoryStart has a genre attribute which is a foreign key to
    the primary key of a Genre Model.
    """
    story_text = models.CharField(max_length=30, unique=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE)

    class Meta:
        """
        Orders the data of the Genre model so that
        it goes by creation date, with the earliest coming
        first.
        """
        ordering = ['creation_date']

    def __str__(self):
        return str(self.story_text)


class StoryMiddle(models.Model):
    """
    Class for the StoryMiddle Model.
    StoryMiddle has a story_text attribute representing the
    middle of a story idea.
    StoryMiddle has a creation_date which is represented
    by DateTime.
    StoryMiddle has a genre attribute which is a foreign key to
    the primary key of a Genre Model.
    """
    story_text = models.CharField(max_length=50, unique=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE)

    class Meta:
        """
        Orders the data of the Genre model so that
        it goes by creation date, with the earliest coming
        first.
        """
        ordering = ['creation_date']

    def __str__(self):
        return str(self.story_text)


class StoryEnd(models.Model):
    """
    Class for the StoryEnd Model.
    StoryEnd has a story_text attribute representing the
    end of a story idea.
    StoryEnd has a creation_date which is represented
    by DateTime.
    StoryEnd has a genre attribute which is a foreign key to
    the primary key of a Genre Model.
    """
    story_text = models.CharField(max_length=60, unique=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE)

    class Meta:
        """
        Orders the data of the Genre model so that
        it goes by creation date, with the earliest coming
        first.
        """
        ordering = ['creation_date']

    def __str__(self):
        return str(self.story_text)


class StoryIdea(models.Model):
    """
    Class for the StoryIdea Model.
    StoryIdea has a user attribute which is a foreign key
    to the primary key of a User Model.
    StoryIdea has a title attribute representing a title.
    StoryIdea has a story_text attribute representing the
    text of a story idea.
    StoryIdea has a creation_date attribute which is
    represented by DateTime.
    StoryIdea has an updated_on attribute which is
    represnted by DateTime.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=15, blank=False)
    story_text = models.CharField(max_length=200, blank=False)
    creation_date = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        """
        Orders the data of the Genre model so that
        it goes by the date on which it was updated,
        with the most recently updated coming first.
        """
        ordering = ['-updated_on']

    def __str__(self):
        return str(self.title)
