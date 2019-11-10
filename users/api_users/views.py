# from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import CustomUserSerializer


@api_view(['POST'],)
def api_registration_view(request):

    if request.method == 'POST':
        serializer = CustomUserSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['response'] = "User successfully registered"
        else:
            data = serializer.errors
        return Response(data)
