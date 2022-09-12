from django.shortcuts import render
from .models import Genre, StoryStart, StoryMiddle, StoryEnd
from .forms import StoryIdeaForm
import random


def get_home_page(request):
    return render(request, 'home.html')

def get_genre_page(request):
    genres = Genre.objects.all()
    context = {
        'genres': genres
    }
    return render(request, 'genre-page.html', context)

def get_genre_type_page(request, id):
    # creates a random sentence that relates to the currently selected genre
    # can be redone with better code

    story_starts = StoryStart.objects.all().filter(genre=id)
    story_starts_list = list(story_starts)
    rand_number = random.randrange(0, len(story_starts_list))
    story_start = story_starts_list[rand_number]

    story_middles = StoryMiddle.objects.all().filter(genre=id)
    story_middles_list = list(story_middles)
    rand_number_two = random.randrange(0, len(story_middles_list))
    story_middle = story_middles_list[rand_number_two]

    story_ends = StoryEnd.objects.all().filter(genre=id)
    story_ends_list = list(story_ends)
    rand_number_three = random.randrange(0, len(story_ends_list))
    story_end = story_ends_list[rand_number_three]

    context = {
        'story_start': story_start,
        'story_middle': story_middle,
        'story_end': story_end,
        'story_idea_form': StoryIdeaForm()
    }


    return render(request, 'genre-type.html', context)


def get_my_stories_page(request, id):

    return render(request, 'my-stories.html')

    
    
