from rest_framework import serializers
from .models import CloudService

class CloudServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = CloudService
        fields = '__all__'
