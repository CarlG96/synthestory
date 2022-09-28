"""
Code for registering models to the
admin site for CRUD functionality for
the admin.
"""
from django.contrib import admin
from .models import Genre, StoryStart, StoryMiddle, StoryEnd, StoryIdea

admin.site.register(Genre)
admin.site.register(StoryStart)
admin.site.register(StoryMiddle)
admin.site.register(StoryEnd)
admin.site.register(StoryIdea)
