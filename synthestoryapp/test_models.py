"""
Code for testing models in Django.
"""
from django.test import TestCase
from synthestoryapp import models


class TestModels(TestCase):

    def test_genre_defaults_to_placeholder(self):
        """
        Function to test whether a Genre model created in the database 
        without an image will default to 'placeholder'.
        """
        genre = models.Genre.objects.create()
        self.assertTrue(genre.genre_image == 'placeholder')