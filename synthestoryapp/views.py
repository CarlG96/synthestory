from django.shortcuts import render, redirect, get_object_or_404
from .models import Genre, StoryStart, StoryMiddle, StoryEnd, StoryIdea, User
from .forms import StoryIdeaForm
from django.contrib.auth.decorators import login_required
import random


def get_home_page(request):
    return render(request, 'index.html')

@login_required
def get_genre_page(request):
    genres = Genre.objects.all()
    context = {
        'genres': genres
    }
    return render(request, 'genre-page.html', context)

@login_required
def get_genre_type_page(request, id):
    if request.method == 'POST':
        title = request.POST.get('title')
        story_text = request.POST.get('story_text')
        StoryIdea.objects.create(title=title, story_text=story_text, user=request.user)

        return render(request, 'index.html')
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

    initial_data = {
        'story_text': f'{story_start} {story_middle} {story_end}'
    }
    form = StoryIdeaForm(initial=initial_data)
    context = {
        'story_idea_form': form
    }

    return render(request, 'genre-type.html', context)

# login required decorator not used due to redirecting to a url with
# 'None' in if 'My Stories' clicked on
def get_my_stories_page(request, id):
    # Prevents user from accessing other users stories
    print(id)
    print(request.user.id)
    if request.user.is_authenticated and str(request.user.id) == id:

        story_ideas = StoryIdea.objects.all().filter(user = request.user.id)
            
        context = {
            'story_ideas': story_ideas
        }
        return render(request, 'my-stories.html', context)

    else: 
        # returns user to homepage if they try to access other user's stories
        return redirect('account_login')

@login_required
def get_my_stories_idea(request, id, idea_id):
   
    if request.user.is_authenticated and str(request.user.id) == id:
        story_idea = StoryIdea.objects.get(id = idea_id)
        if request.method == 'POST':
            form = StoryIdeaForm(request.POST, instance = story_idea)
            if form.is_valid():
                form.save()
                return redirect('home')

        initial_data = {
            'title': f'{story_idea.title}',
            'story_text': f'{story_idea.story_text}'
        }

        form = StoryIdeaForm(initial=initial_data)
        context = {
            'story_idea': story_idea,
            'story_idea_form': form
        }

        return render(request, 'story_idea.html', context)

    else: 
        # returns user to homepage if they try to access other user's stories
        return redirect('account_login')


@login_required
def delete_my_stories_idea(request, id, idea_id):
    story_idea = get_object_or_404(StoryIdea, id = idea_id)
    
    story_idea.delete()
    
    return redirect('home')
    
    
