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
