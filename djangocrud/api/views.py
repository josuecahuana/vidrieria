from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializer import GlassSerializer
from .models import Glass
# Create your views here.
class GlassViewSet(viewsets.ModelViewSet):
    queryset = Glass.objects.all()
    serializer_class = GlassSerializer