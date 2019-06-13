from django.shortcuts import render
from rest_framework import viewsets
from .models import users
from .serializers import usersSerializer

class usersView(viewsets.ModelViewSet):
    queryset  = users.objects.all()
    serializer_class = usersSerializer

class loginView(viewsets.ReadOnlyModelViewSet):
    serializer_class = usersSerializer
    def get_queryset(self):
        querySet = users.objects.all()
        userName = self.request.query_params.get("emailId",'')
        password = self.request.query_params.get("password",'')
        isUserExist = querySet.filter(emailId=userName,password=password)
        return isUserExist
    
   