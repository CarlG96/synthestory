"""
Code for testing models in Django.
"""
from django.test import TestCase
from django.contrib.auth import get_user_model
from synthestoryapp import models


class TestModels(TestCase):

    def setUp(self):
        username = 'BobTheBuilder'
        password = 'HelloWorld1234'
        self.user = get_user_model().objects.create_user(
            username=username,
            password=password
        )

    def test_genre_defaults_to_placeholder(self):
        """
        Function to test whether a Genre model created in the database 
        without an image will default to 'placeholder'.
        """
        genre = models.Genre.objects.create()
        self.assertTrue(genre.genre_image == 'placeholder')

    def test_title_is_returned_with_story_idea_str_method(self):
        story_idea = models.StoryIdea.objects.create(title='Bob', story_text='TheBuilder', user=self.user)
        self.assertTrue(story_idea.__str__() == 'Bob')

    # def test_story_text_is_returned_with_story_start_str_method(self):
