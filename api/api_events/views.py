from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import EventSerializer
from users.models import CustomUser
from api.models import Event, Agent, Environment


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

    # Get user's IP
    request_data = request.META.get('HTTP_X_FORWARDED_FOR')
    if request_data:
        user_ip = request_data.split(',')[0]
    else:
        user_ip = request.META.get('REMOTE_ADDR')

    print(f'> POST request from { user_ip }')

    user_env = request.data['env']
    user_version = request.data['version']

    try:
        env = Environment.objects.get(name=user_env)
    except Environment.DoesNotExist:
        return Response(status=status.HTTP_412_PRECONDITION_FAILED)

    try:
        agent = Agent.objects.get(
            address=user_ip,
            version=user_version,
            env=env.pk
        )
    except Agent.DoesNotExist:
        agent = Agent.objects.create(
            address=user_ip,
            version=user_version,
            env=env
        )

    user = CustomUser.objects.get(pk=4)

    event = Event(user=user, agent=agent)

    if request.method == "POST":
        serializer = EventSerializer(event, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_401_BAD_REQUEST)
