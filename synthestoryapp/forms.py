from .models import StoryIdea
from django import forms

class StoryIdeaForm(forms.ModelForm):
    class Meta:
        model = StoryIdea
        fields = ('title', 'story_text')
        