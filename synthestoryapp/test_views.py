"""
Code for testing views in Django.
"""
from django.test import TestCase
from django.contrib.auth import get_user_model
from synthestoryapp import models


class TestLoggedInViews(TestCase):
    """
    Unit tests to test the views and urls
    when logged in.
    Parameters for each test:
    self: The class itself.
    """

    def setUp(self):
        """
        Standard TestCase setUp
        function. Creates two users for the
        test database and also creates a
        Genre and a StoryStart, StoryMiddle
        and StoryEnd
        for the database so the
        test suite can function properly.
        """
        username = 'BobTheBuilder'
        password = 'HelloWorld1234'
        self.user = get_user_model().objects.create_user(
            username=username,
            password=password
        )
        login = self.client.login(username=username, password=password)
        self.assertTrue(login)

        second_username = 'PatThePostMan'
        second_password = 'GoodbyeMoon1234'
        self.second_user = get_user_model().objects.create_user(
            username=second_username,
            password=second_password
        )
        genre = models.Genre.objects.create(genre_title='testgenre')
        # PEP8 recognises the following as unused variables
        # however they are necessary for the test suite to function
        # correctly.
        story_start = models.StoryStart.objects.create(
                                                    story_text='Hello World',
                                                    genre=genre)
        story_middle = models.StoryMiddle.objects.create(
                                                    story_text='Hello World',
                                                    genre=genre)
        story_end = models.StoryEnd.objects.create(
                                                    story_text='Hello World',
                                                    genre=genre)

    def test_get_home_page(self):
        """
        Tests whether the client request
        gets a 200 response and returns the
        'index.html' template when going to
        the home page whilst logged in.
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_get_genre_page(self):
        """
        Tests whether the client request
        gets a 200 response and returns the
        'genre-page.html' template when going
        to the Genre Page as a logged in user.
        """
        response = self.client.get('/genre-page/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'genre-page.html')

    def test_get_genre_type_page(self):
        """
        Tests whether the client request
        gets a 200 response when logged in and attempting
        to access a Genre Type page and that it returns
        a page with the template: 'genre-type.html'.
        """
        response = self.client.get('/genre-type/1/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'genre-type.html')

    def test_get_my_stories_page(self):
        """
        Tests whether the client request gets a 200 response
        when logged in and attempting to access the My Stories
        page connected to them. Also tests whether it
        returns the 'my-stories.html' template.
        """
        response = self.client.get(f'/my-stories/{self.user.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'my-stories.html')

    def test_get_my_story_idea_page(self):
        """
        Tests whether the client request gets a 200 response
        when trying to access a Story Idea page on their My Stories
        account that is connected with their profile. Also tests
        whether the 'story-idea.html' template is used.
        """
        story_idea = models.StoryIdea.objects.create(title='Bob',
                                                     story_text='TheBuilder',
                                                     user=self.user)
        response = self.client.get(
                                f'/my-stories/{self.user.id}/{story_idea.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'story-idea.html')

    def test_my_stories_protection(self):
        """
        Tests whether the client request gets a 403 response when the user
        tries to access someone else's My Stories page. Also makes
        sure the user is then redirected to a page using the
        '403.html' template.
        """
        response = self.client.get(f'/my-stories/{self.second_user.id}/')
        self.assertTrue(response.status_code, 403)
        self.assertTemplateUsed(response, '403.html')

    def test_story_idea_protection(self):
        """
        Tests whether the client request gets a 403 response when the user
        tries to access someone else's Story Idea. Also makes
        sure the user is then redirected to a page using the
        '403.html' template.
        """
        story_idea = models.StoryIdea.objects.create(title='Pat',
                                                     story_text='ThePostman',
                                                     user=self.second_user)
        response = self.client.get(
                        f'/my-stories/{self.second_user.id}/{story_idea.id}/')
        self.assertTrue(response.status_code, 403)
        self.assertTemplateUsed(response, '403.html')


class TestLoggedOutViews(TestCase):
    """
    Unit tests to test the views and urls
    when not logged in.
    Parameters for each test:
    self: The class itself.
    """
    def setUp(self):
        """
        Standard TestCase setUp
        function. Creates a user for the
        test database and also creates a
        Genre and a StoryStart, StoryMiddle
        and StoryEnd
        for the database so the
        test suite can function properly.
        """
        self.user = get_user_model().objects.create_user(
            username='BobTheBuilder',
            password='HelloWorld1234'
        )
        genre = models.Genre.objects.create(genre_title='testgenre')
        # PEP8 recognises the following as unused variables
        # however they are necessary for the test suite to function
        # correctly.
        story_start = models.StoryStart.objects.create(
                                                    story_text='Hello World',
                                                    genre=genre)
        story_middle = models.StoryMiddle.objects.create(
                                                    story_text='Hello World',
                                                    genre=genre)
        story_end = models.StoryEnd.objects.create(
                                                   story_text='Hello World',
                                                   genre=genre)

    def test_get_home_page(self):
        """
        Tests whether the client request
        gets a 200 response and returns the
        'index.html' template when going to
        the home page whilst not logged in.
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_get_genre_page_redirect(self):
        """
        Tests whether the client request gets
        a 302 response when attempting to access the
        Genre page when not logged in.
        """
        response = self.client.get('/genre-page/')
        self.assertEqual(response.status_code, 302)

    def test_get_genre_type_page_redirect(self):
        """
        Tests whether the client request gets
        a 302 response when attempting to access the
        Genre Type page when not logged in.
        """
        response = self.client.get('/genre-type/1/')
        self.assertEqual(response.status_code, 302)

    def test_get_my_stories_page_redirect(self):
        """
        Tests whether the client request gets
        a 302 response when attempting to access the
        My Stories page when not logged in.
        """
        response = self.client.get(f'/my-stories/{self.user.id}/')
        self.assertEqual(response.status_code, 302)

    def test_get_story_idea_redirect(self):
        """
        Tests whether the client request gets
        a 302 response when attempting to access a
        Story Idea page when not logged in.
        """
        story_idea = models.StoryIdea.objects.create(title='Bob',
                                                     story_text='TheBuilder',
                                                     user=self.user)
        response = self.client.get(
                              f'/my-stories/{self.user.id}/{story_idea.id}/')
        self.assertEqual(response.status_code, 302)
