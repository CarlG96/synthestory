"""
Code for testing models in Django.
"""
from django.test import TestCase
from django.contrib.auth import get_user_model
from synthestoryapp import models


class TestModels(TestCase):
    """
    Unit tests to test the Models.
    Parameters for each test:
    self: The class itself.
    """
    def setUp(self):
        """
        Standard TestCase setUp
        function. Creates a user for the
        test database and also creates a
        Genre for the database so the
        test suite can function properly.
        """
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

    def test_title_is_returned_with_genre_str_method(self):
        """
        Function that tests the __str__ method
        for Genre. Checks whether it
        returns the correct string.
        """
        story_idea = models.Genre.objects.create(genre_title='Bob')
        self.assertTrue(story_idea.__str__() == 'Bob')

    def test_title_is_returned_with_story_idea_str_method(self):
        """
        Function that tests the __str__ method
        for StoryIdea. Checks whether it
        returns the correct string.
        """
        story_idea = models.StoryIdea.objects.create(title='Bob',
                                                     story_text='TheBuilder',
                                                     user=self.user)
        self.assertTrue(story_idea.__str__() == 'Bob')

    def test_story_text_is_returned_with_story_start_str_method(self):
        """
        Function that tests the __str__ method
        for StoryStart. Checks whether it
        returns the correct string.
        """
        story_start = models.StoryStart.objects.create(
                                                      story_text='Hello World',
                                                      genre=self.genre)
        self.assertTrue(story_start.__str__() == 'Hello World')

    def test_story_text_is_returned_with_story_middle_str_method(self):
        """
        Function that tests the __str__ method
        for StoryMiddle. Checks whether it
        returns the correct string.
        """
        story_middle = models.StoryMiddle.objects.create(
                                                    story_text='Hello World',
                                                    genre=self.genre)
        self.assertTrue(story_middle.__str__() == 'Hello World')

    def test_story_text_is_returned_with_story_end_str_method(self):
        """
        Function that tests the __str__ method
        for StoryEnd. Checks whether it
        returns the correct string.
        """
        story_end = models.StoryEnd.objects.create(story_text='Hello World',
                                                   genre=self.genre)
        self.assertTrue(story_end.__str__() == 'Hello World')
