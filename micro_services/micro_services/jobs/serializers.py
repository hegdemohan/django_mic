from rest_framework import serializers
from .models import jobs

class jobsSerializer(serializers.ModelSerializer):
    class Meta:
        model= jobs
        # fields= ('userName','passWord','id')
        fields= ('__all__')
