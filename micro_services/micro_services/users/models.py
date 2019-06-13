from django.db import models

# Create your models here.

class users(models.Model):
    user_id = models.AutoField(primary_key=True)
    emailId= models.CharField(unique=True,max_length=100)
    password= models.CharField(max_length=100)
    firstName= models.CharField(max_length=100)
    lastName= models.CharField(max_length=100)
    phoneNumber= models.CharField(max_length=100)
    rating= models.FloatField()
    totalRatings= models.IntegerField();
    address= models.TextField()

    def __str__(self):
        return str(self.user_id);