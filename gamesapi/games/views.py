from django.contrib.auth import authenticate
from django.http import JsonResponse
from django.core import serializers as core_serializers
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response
from rest_framework import routers, serializers, viewsets
from gamesapi.serializers import GameSerializer
from games.models import Game


@api_view(["GET"])
@permission_classes((AllowAny,))
def index(request):
    return JsonResponse("Welcome to Games Listing API!", safe=False)


@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'}, status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key}, status=HTTP_200_OK)


@api_view(["GET"])
@permission_classes((IsAuthenticated,))
def search(request, title):
    data = Game.objects.filter(title=title).values()
    if len(data) == 0:
        return Response("No matching game found", HTTP_400_BAD_REQUEST)
    else:
        return Response(data, status=HTTP_200_OK)


@permission_classes((IsAuthenticated,))
class GameViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,)
    queryset = Game.objects.all()
    serializer_class = GameSerializer
