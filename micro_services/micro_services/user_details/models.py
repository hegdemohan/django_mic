from django.db import models

# Create your models here.

class user_details(models.Model):
    emailId= models.CharField(max_length=100)
    firstName= models.CharField(max_length=100)
    lastName= models.CharField(max_length=100)

    def __str__(self):
        return self.emailId;