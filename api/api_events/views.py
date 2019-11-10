from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import EventSerializer
from users.models import CustomUser
from api.models import Event, Agent


@api_view(['GET', ])
def api_detail_event_view(request, level):

    try:
        event = Event.objects.get(level=level)
    except Event.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = EventSerializer(event)
        return Response(serializer.data)


@api_view(['POST', ])
def api_create_event_view(request):

    user = CustomUser.objects.get(pk=1)
    agent = Agent.objects.get(pk=1)

    event = Event(user=user, agent=agent)

    if request.method == "POST":
        serializer = EventSerializer(event, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_401_BAD_REQUEST)
