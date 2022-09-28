"""
Code for testing views in Django.
"""
from django.test import TestCase
from django.contrib.auth import get_user_model
from synthestoryapp import views, models


class TestLoggedInViews(TestCase):

    def setUp(self):
        username = 'BobTheBuilder'
        password = 'HelloWorld1234'
        user = get_user_model()
        self.user = user.objects.create_user(
            username=username,
            password=password
        )
        login = self.client.login(username=username, password=password)
        self.assertTrue(login)

        genre = models.Genre.objects.create(genre_title='testgenre')
        story_start = models.StoryStart.objects.create(story_text='Hello World', genre=genre)
        story_middle = models.StoryMiddle.objects.create(story_text='Hello World', genre=genre)
        story_end = models.StoryEnd.objects.create(story_text='Hello World', genre=genre)
        story_idea = models.StoryIdea.objects.create(title='Bob', story_text='TheBuilder', user=self.user)

    def test_get_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
    
    def test_get_genre_page(self):
        response = self.client.get('/genre-page/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'genre-page.html')

    def test_get_genre_type_page(self):
        response = self.client.get('/genre-type/1/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'genre-type.html')

    def test_get_my_stories_page(self):
        response = self.client.get('/my-stories/1/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'my-stories.html')

    def test_get_my_story_idea_page(self):
        response = self.client.get('/my-stories/1/1/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'story-idea.html')

# class TestLoggedOutViews(TestCase):
