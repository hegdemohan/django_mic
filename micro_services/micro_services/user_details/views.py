from django.shortcuts import render
from rest_framework import viewsets
from .models import user_details
from .serializers import userSerializer

class userDetails(viewsets.ModelViewSet):
    queryset  = user_details.objects.all()
    serializer_class = userSerializer