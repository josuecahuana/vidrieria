from dataclasses import field
from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Glass

class GlassSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Glass
        fields = ['nombre','costo','tipo','largo','alto','grosor','id','imagen']
