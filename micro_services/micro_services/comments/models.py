from django.db import models
from jobs.models import jobs
from users.models import users

# Create your models here.

class comments(models.Model):
    comment_id = models.AutoField(primary_key=True)
    job_id = models.ForeignKey(jobs, on_delete=models.CASCADE)
    user_id = models.ForeignKey(users, on_delete=models.CASCADE)
    comment = models.CharField(max_length=100)

    def __str__(self):
        return str(self.comment_id);