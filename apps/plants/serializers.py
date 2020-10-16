from django.contrib.auth.models import User
from rest_framework import serializers

from django.contrib.auth.models import User

from apps.plants.models import Plant, UserPlant


class PlantSerializer(serializers.ModelSerializer):

    class Meta:
        model = Plant
        fields = ['id', 'latin_name', 'polish_name', 'image']

class UserPlantSerializer(serializers.ModelSerializer):
    plant = PlantSerializer(read_only=True, many=False)
    plant_id = serializers.IntegerField(write_only=True)
    class Meta:
        model = UserPlant
        fields = ['id', 'name','plant',  'plant_id']