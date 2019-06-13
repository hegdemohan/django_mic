from django.db import models

# Create your models here.

class jobs(models.Model):
    job_id = models.AutoField(primary_key=True)
    job_title= models.CharField(max_length=100)
    description= models.CharField(max_length=100)
    date= models.CharField(max_length=100)
    salary= models.FloatField()
    category= models.CharField(max_length=100)
    address= models.TextField()

    def __str__(self):
        return str(self.job_id);