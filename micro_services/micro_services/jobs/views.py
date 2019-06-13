from django.shortcuts import render
from rest_framework import viewsets
from .models import jobs
from users.models import users
from roles.models import roles
from roles.serializers import rolesSerializer
from .serializers import jobsSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

class jobsView(viewsets.ModelViewSet):
    queryset  = jobs.objects.all()
    serializer_class = jobsSerializer

def getAllRoles(user_id,role):
    querySet = roles.objects.all()
    return querySet.filter(user_id=user_id,role=role)

def getJob(job_id):
    querySetJob = jobs.objects.all()
    return querySetJob.filter(job_id=job_id)

def appendQuerySet(allJobs,job):
    return allJobs | job
    
class getPublishedJobs(viewsets.ReadOnlyModelViewSet):
    serializer_class = jobsSerializer
    def get_queryset(self):
        querySet = ''
        allJobs = jobs.objects.none()
        user_id = self.request.query_params.get("user_id",'')
        rolesList = getAllRoles(user_id,"Publisher")
        for role in rolesList:
            job = getJob(role.__dict__['job_id_id'])
            allJobs = appendQuerySet(allJobs,job)
        return allJobs