from django.shortcuts import render
from django.views import generic
from .models import Genre


class LandingPageView(generic.ListView):
    model = Genre
    template_name = 'index.html'