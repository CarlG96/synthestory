from django.contrib import admin
from .models import Genre, StoryStart, StoryMiddle, StoryEnd

admin.site.register(Genre)
admin.site.register(StoryStart)
admin.site.register(StoryMiddle)
admin.site.register(StoryEnd)


# Register your models here.
