from django.shortcuts import render
from rest_framework import viewsets
from .models import users
from roles.models import roles
from .serializers import usersSerializer
from roles.serializers import rolesSerializer
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

class getUserDetailsView(viewsets.ReadOnlyModelViewSet):
    serializer_class = usersSerializer
    def get_queryset(self):
        querySet = roles.objects.all()
        job_id = self.request.query_params.get("job_id",'') 
        job_details = querySet.filter(job_id=job_id,role='Publisher')
        allUsers = users.objects.all()
        user = allUsers.filter(user_id=job_details[0].__dict__['user_id_id'])
        return user

    
   