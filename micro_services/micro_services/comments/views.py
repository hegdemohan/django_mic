from django.shortcuts import render
from rest_framework import viewsets
from .models import comments
from .serializers import commentsSerializer

class commentsView(viewsets.ModelViewSet):
    queryset  = comments.objects.all()
    serializer_class = commentsSerializer