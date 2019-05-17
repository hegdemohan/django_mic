from rest_framework import serializers
from .models import user_details

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model= user_details
        # fields= ('userName','passWord','id')
        fields= ('__all__')
