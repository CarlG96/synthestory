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
        self.user = get_user_model().objects.create_user(
            username=username,
            password=password
        )
        login = self.client.login(username=username, password=password)
        self.assertTrue(login)

        genre = models.Genre.objects.create(genre_title='testgenre')
        story_start = models.StoryStart.objects.create(story_text='Hello World', genre=genre)
        story_middle = models.StoryMiddle.objects.create(story_text='Hello World', genre=genre)
        story_end = models.StoryEnd.objects.create(story_text='Hello World', genre=genre)

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
        response = self.client.get(f'/my-stories/{self.user.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'my-stories.html')

    def test_get_my_story_idea_page(self):
        story_idea = models.StoryIdea.objects.create(title='Bob', story_text='TheBuilder', user=self.user)
        response = self.client.get(f'/my-stories/{self.user.id}/{story_idea.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'story-idea.html')

    # def test_403_protection(self):
    #     username = 'PatThePostman'
    #     password = 'GoodbyeMoon1234'
    #     print(self.user.id)
    #     second_user = get_user_model().objects.create_user(
    #         username=username,
    #         password=password
    #     )
    #     story_idea = models.StoryIdea.objects.create(title='Pat', story_text='ThePostman', user=second_user)

    #     response = self.client.get(f'/my-stories/{second_user.id}/')
    #     self.assertEqual(response.status_code, 403)

class TestLoggedOutViews(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='BobTheBuilder',
            password='HelloWorld1234'
        )
        genre = models.Genre.objects.create(genre_title='testgenre')
        story_start = models.StoryStart.objects.create(story_text='Hello World', genre=genre)
        story_middle = models.StoryMiddle.objects.create(story_text='Hello World', genre=genre)
        story_end = models.StoryEnd.objects.create(story_text='Hello World', genre=genre)

    def test_get_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_get_genre_page_redirect(self):
        response = self.client.get('/genre-page/')
        self.assertEqual(response.status_code, 302)

    def test_get_genre_type_page_redirect(self):
        response = self.client.get('/genre-type/1/')
        self.assertEqual(response.status_code, 302)

    def test_get_my_stories_page_redirect(self):
        response = self.client.get(f'/my-stories/{self.user.id}/')
        self.assertEqual(response.status_code, 302)

    def test_get_story_idea_redirect(self):
        story_idea = models.StoryIdea.objects.create(title='Bob', story_text='TheBuilder', user=self.user)
        response = self.client.get(f'/my-stories/{self.user.id}/{story_idea.id}/')
        self.assertEqual(response.status_code, 302)