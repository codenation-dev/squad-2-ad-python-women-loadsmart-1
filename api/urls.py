from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.EventsView.as_view(), name='events_list'),
    # path('events/detail', views.events_detail, name='events_detail'),
    url(r'events/detail/(?P<pk>[-\w]+)', views.EventDetailView.as_view(), name='events_detail'),
]
