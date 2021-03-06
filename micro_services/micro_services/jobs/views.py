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
    queryset  = jobs.objects.order_by('-job_id')
    serializer_class = jobsSerializer

def getAllRoles(user_id,role):
    querySet = roles.objects.all()
    return querySet.filter(user_id=user_id,role=role)

def getJob(job_id):
    querySetJob = jobs.objects.all()
    return querySetJob.filter(job_id=job_id)

def appendQuerySet(allJobs,job):
    return allJobs | job
    
class getJobs(viewsets.ReadOnlyModelViewSet):
    serializer_class = jobsSerializer
    def get_queryset(self):
        querySet = ''
        allJobs = jobs.objects.none()
        user_id = self.request.query_params.get("user_id",'')
        user_role = self.request.query_params.get("role",'')
        rolesList = getAllRoles(user_id,user_role)
        for role in rolesList:
            job = getJob(role.__dict__['job_id_id'])
            allJobs = appendQuerySet(allJobs,job)
        return allJobs

class jobSearch(viewsets.ReadOnlyModelViewSet):
    serializer_class = jobsSerializer
    def get_queryset(self):
        querySet = ''
        jobList = jobs.objects.all()
        search_Text = self.request.query_params.get("searchText","")
        category = self.request.query_params.get("category","")
        if category !="All":
            return jobList.filter(job_title__icontains=search_Text,category__icontains=category).order_by('-job_id')
        else:
            return jobList.filter(job_title__icontains=search_Text).order_by('-job_id')