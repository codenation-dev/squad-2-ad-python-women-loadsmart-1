from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect

from .models import Event


class EventsView(LoginRequiredMixin, ListView):
    model = Event
    template_name = 'events/list.html'
    queryset = Event.objects.exclude(archived=True).order_by('-date')
    # paginate_by = 5

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


def mark_as_archived(request):
    if request.method == "POST":
        selected_events = request.POST.getlist('arch_checkbox')
        print(selected_events)
        amount_updated = Event.objects.filter(id__in=selected_events).update(archived=True)
        print("Number of events archived: {amount_updated}")
    return redirect('events_list')
