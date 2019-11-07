from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Event


class EventsView(ListView):
    model = Event
    template_name = 'events/list.html'


class EventDetailView(DetailView):
  model = Event
  template_name = 'events/detail.html'
