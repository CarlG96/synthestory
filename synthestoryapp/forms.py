"""
Code for classes involving
forms
"""
from django.forms import Textarea
from django import forms
from .models import StoryIdea


class StoryIdeaForm(forms.ModelForm):
    """
    Form for StoryIdea
    """
    class Meta:
        """
        Information about fields
        and labels
        Attributes:
        model (class): Class of StoryIdea used to make
        form.
        fields (tuple of str): Designates fields for
        form.
        widgets (dictionary): Designates size of textareas.
        labels (dictionary): Adds labels to form.
        """
        model = StoryIdea
        fields = ('title', 'story_text')
        widgets = {
            'title': Textarea(attrs={'rows': 1, 'cols': 20}),
            'story_text': Textarea(attrs={'rows': 8, 'cols': 20}),
        }
        labels = {
            'title': 'Title',
            'story_text': 'Story Idea'
        }
