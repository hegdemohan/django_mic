from django.shortcuts import render
from rest_framework import viewsets
from .models import comments
from .serializers import commentsSerializer
from .serializers import allCommentSerializer
from rest_framework import generics

class commentsView(viewsets.ModelViewSet):
    queryset  = comments.objects.all()
    serializer_class = commentsSerializer

class getComments(viewsets.ReadOnlyModelViewSet):
    serializer_class = commentsSerializer
    def get_queryset(self):
        querySet = comments.objects.all()
        job_id = self.request.query_params.get("job_id",'')
        print(querySet)
        return querySet.filter(job_id=job_id)