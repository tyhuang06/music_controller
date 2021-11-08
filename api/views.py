from asyncio.format_helpers import _get_function_source
from xmlrpc.client import GzipDecodedResponse
from django.shortcuts import render
from rest_framework import generics
from .serializers import RoomSerializer
from .models import Room

# Create your views here.
class RoomView(generics.ListAPIView):
    queryset = Room.objects.all
    serializer_class = RoomSerializer
