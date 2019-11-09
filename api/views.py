from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Event


class EventsView(LoginRequiredMixin, ListView):
    model = Event
    template_name = 'events/list.html'


class EventDetailView(LoginRequiredMixin, DetailView):
    model = Event
    template_name = 'events/detail.html'
