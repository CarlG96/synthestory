from . import views
from .views import get_genre_page, get_genre_type_page, get_home_page, get_my_stories_page, get_my_stories_idea, delete_my_stories_idea
from django.urls import path

urlpatterns = [
    path('', get_home_page, name='home'),
    path('genre-page/', get_genre_page, name='genre-page'),
    path('genre-type/<str:id>/', get_genre_type_page, name='genre-type'),
    path('my-stories/<str:id>/', get_my_stories_page, name='my-stories'),
    path('my-stories/<str:id>/<str:idea_id>/', get_my_stories_idea, name='my-stories-idea'),
    path('delete/<str:id>/<str:idea_id>/', delete_my_stories_idea, name='delete-stories-idea')
]
