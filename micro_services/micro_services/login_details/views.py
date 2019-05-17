from django.shortcuts import render
from rest_framework import viewsets
from .models import login_details
from .serializers import loginSerializer

class loginDetails(viewsets.ModelViewSet):
    queryset  = login_details.objects.all()
    serializer_class = loginSerializer