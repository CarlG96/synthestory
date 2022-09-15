from .models import StoryIdea
from django import forms
from django.forms import Textarea

class StoryIdeaForm(forms.ModelForm):

    class Meta:
        model = StoryIdea
        fields = ('title', 'story_text')
        widgets = {
            'title': Textarea(attrs={'rows':1, 'cols':20}),
            'story_text': Textarea(attrs={'rows':8, 'cols':20}),
        }
        labels = {
            'title': 'Title',
            'story_text': 'Story Idea'
        }
        