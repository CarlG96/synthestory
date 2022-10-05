"""
Code for Django url routing
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_home_page, name='home'),
    path('genre-page/', views.get_genre_page, name='genre-page'),
    path('genre-type/<str:id_num>/', views.get_genre_type_page,
         name='genre-type'),
    path('my-stories/<str:id_num>/', views.get_my_stories_page,
         name='my-stories'),
    path('my-stories/<str:id_num>/<str:idea_id>/', views.get_my_stories_idea,
         name='my-stories-idea'),
    path('delete/<str:id_num>/<str:idea_id>/', views.delete_my_stories_idea,
         name='delete-stories-idea')
]
