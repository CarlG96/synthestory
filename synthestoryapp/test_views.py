"""
Code for testing views in Django.
"""
from django.test import TestCase
from synthestoryapp import views


class TestViews(TestCase):

    def test_get_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
    
    def test_get_genre_page(self):
        response = self.client.get('/genre-page')
        self.assertEqual(response.status_code, 200)

    # def test_get_type_page(self):

    # def test_get_my_stories_page(self):

    # def test_get_my_story_idea_page(self):