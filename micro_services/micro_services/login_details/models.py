from django.db import models

# Create your models here.

class login_details(models.Model):
    emailId= models.CharField(max_length=100)
    password= models.CharField(max_length=100)
    securityQuestion= models.CharField(max_length=100)
    answer= models.CharField(max_length=100)

    def __str__(self):
        return self.emailId;