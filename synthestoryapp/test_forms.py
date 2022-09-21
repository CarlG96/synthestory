"""
Code for testing forms in Django
"""
from django.test import TestCase
from .forms import StoryIdeaForm


class TestStoryIdeaForm(TestCase):
    """
    Unit tests to test the StoryIdeaForm.
    """

    def test_title_is_required(self):
        """
        Tests whether the StoryIdeaForm can
        have a blank title attribute. Should
        not be able to.
        """
        form = StoryIdeaForm({'title': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors.keys())
        self.assertEqual(form.errors['title'][0], 'This field is required.')

    def test_story_text_is_required(self):
        """
        Tests whether the StoryIdeaForm can
        have a blank title attribute. Should
        not be able to.
        """
        form = StoryIdeaForm({'story_text': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('story_text', form.errors.keys())
        self.assertEqual(form.errors['story_text'][0],
                         'This field is required.')

    def test_fields_are_in_meta(self):
        """
        Tests whether the fields in the Meta Class are
        'title' and 'story_text'. Should be true.
        """
        form = StoryIdeaForm()
        self.assertEqual(form.Meta.fields, ('title', 'story_text'))

    def test_valid_form(self):
        """
        Tests whether a form with both a title and
        a story_text value should be valid. Should be
        true.
        """
        form = StoryIdeaForm({
            'title': 'Title',
            'story_text': 'This is story text'
        })
        self.assertTrue(form.is_valid())
