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
        self.genre = models.Genre.objects.create(genre_title='testgenre')

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

    def test_story_text_is_returned_with_story_start_str_method(self):
        story_start = models.StoryStart.objects.create(story_text='Hello World', genre=self.genre)
        self.assertTrue(story_start.__str__() == 'Hello World')


    def test_story_text_is_returned_with_story_middle_str_method(self):
        story_middle = models.StoryMiddle.objects.create(story_text='Hello World', genre=self.genre)
        self.assertTrue(story_middle.__str__() == 'Hello World')


    def test_story_text_is_returned_with_story_end_str_method(self):
        story_end = models.StoryEnd.objects.create(story_text='Hello World', genre=self.genre)
        self.assertTrue(story_end.__str__() == 'Hello World')
