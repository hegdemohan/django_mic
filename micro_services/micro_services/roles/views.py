from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from rest_framework import viewsets
from .models import roles
from jobs.models import jobs
from users.models import users
from .serializers import rolesSerializer
from jobs.serializers import jobsSerializer

class rolesView(viewsets.ModelViewSet):
    queryset  = roles.objects.all()
    serializer_class = rolesSerializer

class checkUserRole(viewsets.ReadOnlyModelViewSet):
    serializer_class = rolesSerializer
    def get_queryset(self):
        querySet = roles.objects.all()
        user_id = self.request.query_params.get('user_id','')
        job_id = self.request.query_params.get('job_id','')
        return querySet.filter(user_id_id=user_id,job_id_id=job_id)


class sendMail(viewsets.ReadOnlyModelViewSet):
    serializer_class = jobsSerializer
    def get_queryset(self):
        querySet = jobs.objects.none()
        allJobs = jobs.objects.all()
        allUsers= users.objects.all()
        job_id = self.request.query_params.get("job_id",'')
        applied_job = allJobs.filter(job_id=job_id)
        publisher_id = self.request.query_params.get("publisher_id",'')
        publisher_details = allUsers.filter(user_id=publisher_id)
        applicant_id = self.request.query_params.get("applicant_id",'')
        applicant_details = allUsers.filter(user_id=applicant_id)
        sendEmail(applied_job,publisher_details,applicant_details)
        return querySet

def sendEmail(applied_job,publisher_details,applicant_details):
    subject = "Application for " + applied_job[0].job_title
    message = "Hello " + publisher_details[0].firstName + ' ' + publisher_details[0].lastName + ',\n\nWe would like to inform you that below mentioned user is interested in the job "'+ applied_job[0].job_title +'" published on ' + applied_job[0].date + "\n\nUser Details : \n" + applicant_details[0].firstName + ' ' + applicant_details[0].lastName + '\n' + applicant_details[0].emailId + '\n' + applicant_details[0].phoneNumber + '\n\nThanks & Regards, \nJober Desk'
    from_email= settings.EMAIL_HOST_USER
    to_email=[publisher_details[0].emailId]
    send_mail(
        subject,
        message,
        from_email,
        to_email,
        fail_silently=False,
    )