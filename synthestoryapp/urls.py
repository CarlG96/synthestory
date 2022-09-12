from . import views
from .views import get_genre_page, get_genre_type_page, get_home_page
from django.urls import path

urlpatterns = [
    path('home/', get_home_page, name='home'),
    path('', get_genre_page, name='genre-page'),
    path('genre-type/<str:id>/', get_genre_type_page, name='genre-type'),
    # path('my-stories/<str:id>/', get_my_stories_page, name='my-stories')
]
