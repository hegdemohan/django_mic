from django.shortcuts import render
from rest_framework import viewsets
from .models import roles
from .serializers import rolesSerializer

class rolesView(viewsets.ModelViewSet):
    queryset  = roles.objects.all()
    serializer_class = rolesSerializer