from django.shortcuts import render
from .models import Genre, StoryStart
import random

def get_genre_page(request):
    genres = Genre.objects.all()
    context = {
        'genres': genres
    }
    return render(request, 'genre-page.html', context)

def get_genre_type_page(request):
    story_starts = StoryStart.objects.all()
    story_starts_list = list(story_starts)
    rand_number = random.randrange(0, len(story_starts_list))
    story_start = story_starts_list[rand_number]
    context = {
        'story_start': story_start
    }


    return render(request, 'genre-type.html', context)