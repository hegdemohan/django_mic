from rest_framework import serializers
from .models import roles

class rolesSerializer(serializers.ModelSerializer):
    class Meta:
        model= roles
        # fields= ('role_id','job_id','user_id','role')
        fields= ('__all__')
