from rest_framework import serializers
from .models import comments

class commentsSerializer(serializers.ModelSerializer):
    class Meta:
        model= comments
        # fields= ('userName','passWord','id')
        fields= ('__all__')
