from django.contrib import admin

from .models import Event, Environment, Agent

admin.site.register(Event)
admin.site.register(Agent)
admin.site.register(Environment)