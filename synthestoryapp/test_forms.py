from django.test import TestCase
from .forms import StoryIdeaForm

class TestStoryIdeaForm(TestCase):

    def test_title_is_required(self):
        form = StoryIdeaForm({'title': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors.keys())
        self.assertEqual(form.errors['title'][0], 'This field is required.')