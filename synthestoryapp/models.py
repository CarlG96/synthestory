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
    Attributes:
    genre_title (str): Represents the title for the Genre.
    genre_image (file): An image associated with the Genre.
    genre_description (str): Describes the genre.
    creation_date (DateTime): Date and time of creation of the
    Genre.
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
        Attributes:
        ordering (list): Orders the Genre models.
        """
        ordering = ['creation_date']

    def __str__(self):
        return str(self.genre_title)


class StoryStart(models.Model):
    """
    Class for the StoryStart Model. This model
    represents the start of one of SyntheStory's
    'Story Ideas'.
    Attributes:
    story_text (str): The text of the StoryStart.
    creation_date (DateTime): Date and time of creation of the
    StoryStart.
    genre (ForeignKey): A foreign key which links to the
    primary key of a Genre Model.
    """
    story_text = models.CharField(max_length=30, unique=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE)

    class Meta:
        """
        Orders the data of the Genre model so that
        it goes by creation date, with the earliest coming
        first.
        Attributes:
        ordering (list): Orders the StoryStart models.
        """
        ordering = ['creation_date']

    def __str__(self):
        return str(self.story_text)


class StoryMiddle(models.Model):
    """
    Class for the StoryMiddle Model.
    This model
    represents the middle of one of SyntheStory's
    'Story Ideas'.
    Attributes:
    story_text (str): The text of the StoryMiddle.
    creation_date (DateTime): Date and time of creation of the
    StoryMiddle.
    genre (ForeignKey): A foreign key which links to the
    primary key of a Genre Model.
    """
    story_text = models.CharField(max_length=50, unique=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE)

    class Meta:
        """
        Orders the data of the Genre model so that
        it goes by creation date, with the earliest coming
        first.
        Attributes:
        ordering (list): Orders the StoryMiddle models.
        """
        ordering = ['creation_date']

    def __str__(self):
        return str(self.story_text)


class StoryEnd(models.Model):
    """
    Class for the StoryEnd Model.
    This model
    represents the end of one of SyntheStory's
    'Story Ideas'.
    Attributes:
    story_text (str): The text of the StoryEnd.
    creation_date (DateTime): Date and time of creation of the
    StoryEnd.
    genre (ForeignKey): A foreign key which links to the
    primary key of a Genre Model.
    """
    story_text = models.CharField(max_length=60, unique=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE)

    class Meta:
        """
        Orders the data of the Genre model so that
        it goes by creation date, with the earliest coming
        first.
        Attributes:
        ordering (list): Orders the StoryMiddle models.
        """
        ordering = ['creation_date']

    def __str__(self):
        return str(self.story_text)


class StoryIdea(models.Model):
    """
    Class for the StoryIdea Model.
    This class represents a saved
    'Story Idea' by a user.
    Attributes:
    user (ForeignKey): foreign key to the primary key
    of a User Model.
    title (str): Represents the title for the StoryIdea.
    story_text (str): Represents the
    text of a StoryIdea.
    creation_date (DateTime): Date and time of creation of the
    StoryIdea.
    updated_on (DateTime): Date and time of the most
    recent update to the StoryIdea.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=30, blank=False)
    story_text = models.CharField(max_length=200, blank=False)
    creation_date = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        """
        Orders the data of the Genre model so that
        it goes by the date on which it was updated,
        with the most recently updated coming first.
        Attributes:
        ordering (list): Orders the StoryIdea models.
        """
        ordering = ['-updated_on']

    def __str__(self):
        return str(self.title)
