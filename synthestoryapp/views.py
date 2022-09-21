from django.shortcuts import render, redirect, get_object_or_404
from synthestoryapp import models
from .forms import StoryIdeaForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import random

def random_story_part(model_list, id_number):
    story_parts = model_list.objects.all().filter(genre=id_number)
    story_list = list(story_parts)
    rand_number = random.randrange(0, len(story_list))
    story_part = story_list[rand_number]
    return story_part

def get_home_page(request):
    return render(request, 'index.html')


@login_required
def get_genre_page(request):
    genres = models.Genre.objects.all()
    context = {
        'genres': genres
    }
    return render(request, 'genre-page.html', context)


@login_required
def get_genre_type_page(request, id):
    if request.method == 'POST':
        title = request.POST.get('title')
        story_text = request.POST.get('story_text')
        messages.add_message(request, messages.SUCCESS, f'Successfully added story idea: {title}.')
        models.StoryIdea.objects.create(title=title, story_text=story_text, user=request.user)

        # repeated elsewhere
        story_ideas = models.StoryIdea.objects.all().filter(user = request.user.id)
            
        context = {
            'story_ideas': story_ideas
        }

        return render(request, 'my-stories.html', context)
    # creates a random sentence that relates to the currently selected genre
    # can be redone with better code
    
    story_start = random_story_part(models.StoryStart, id)
    story_middle = random_story_part(models.StoryMiddle, id)
    story_end = random_story_part(models.StoryEnd, id)
    
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

        story_ideas = models.StoryIdea.objects.all().filter(user = request.user.id)
            
        context = {
            'story_ideas': story_ideas
        }
        return render(request, 'my-stories.html', context)

    else: 
        # returns user to homepage if they try to access other user's stories
        return redirect('account_login')


@login_required
def get_my_stories_idea(request, id, idea_id):
    
    # code for editing story
    if request.user.is_authenticated and str(request.user.id) == id:
        story_idea = models.StoryIdea.objects.get(id = idea_id)
        if request.method == 'POST':
            form = StoryIdeaForm(request.POST, instance = story_idea)
            if form.is_valid():
                form.save()
                title = request.POST.get('title')
                messages.add_message(request, messages.WARNING, f'Successfully edited story idea: {title}.')
                # repeated elsewhere
                story_ideas = models.StoryIdea.objects.all().filter(user = request.user.id)
            
                context = {
                'story_ideas': story_ideas
                }

                return render(request, 'my-stories.html', context)

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
    story_idea = get_object_or_404(models.StoryIdea, id = idea_id)
    title = story_idea.title
    story_idea.delete()
    messages.add_message(request, messages.ERROR, f'Successfully deleted story idea: {title}.')
    story_ideas = models.StoryIdea.objects.all().filter(user = request.user.id)
            
    context = {
    'story_ideas': story_ideas
    }

    return render(request, 'my-stories.html', context)
    
    
