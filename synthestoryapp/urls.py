from . import views
from .views import get_genre_page, get_genre_type_page
from django.urls import path

urlpatterns = [
    path('', get_genre_page, name="genre-page"),
    path('genre-type/', get_genre_type_page, name="genre-type")
]
