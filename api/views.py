from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Event


class EventsView(LoginRequiredMixin, ListView):
    model = Event
    template_name = 'events/list.html'

    """ def get_queryset(self, *args, **kwargs):
        search_text: self.request.GET.get('search_text', None)
        search_env: self.request.GET.get('search_env', None)
        search_type: self.request.GET.get('search_type', None)
        ordering: self.request.GET.get('ordering', None)

        object_list = Event.objects.all()
        if ordering is not None and ordering == 'level':
            object_list = sorted(self.model.objects, key=lambda m: m.level)
        if search_env is not None and search_env != '':
            object_list = self.model.objects.filter(
                agent__env=search_env
            )
        if search_type is not None and search_type != '':
            object_list = self.model.objects.filter(
                agent__env=self.env
            )
        else:
            object_list = self.model.objects.all() """


class EventDetailView(LoginRequiredMixin, DetailView):
    model = Event
    template_name = 'events/detail.html'
