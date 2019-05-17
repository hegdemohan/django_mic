from rest_framework import serializers
from .models import login_details

class loginSerializer(serializers.ModelSerializer):
    class Meta:
        model= login_details
        # fields= ('userName','passWord','id')
        fields= ('__all__')
