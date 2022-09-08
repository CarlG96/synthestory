from . import views
from .views import get_genre_page
from django.urls import path

urlpatterns = [
    path('', get_genre_page, name="genre-page"),
]
