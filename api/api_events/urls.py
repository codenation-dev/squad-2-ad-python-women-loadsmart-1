from django.urls import path
from api.api_events import views

app_name = "api"

urlpatterns = [
    path('get/<level>', views.api_detail_event_view, name='api_events_detail'),
    path('create', views.api_create_event_view, name='api_events_create'),
]
