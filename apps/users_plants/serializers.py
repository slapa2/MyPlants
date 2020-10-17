from django.contrib.auth.models import User
from rest_framework import serializers

from rest_framework.fields import ChoiceField

from apps.plants.models import Plant
from apps.plants.serializers import PlantSerializer

from .models import PlantEvent, UserPlant



class PlantEventSerializer(serializers.ModelSerializer):

    user_plant_id = serializers.IntegerField()
    event = serializers.ChoiceField(choices=PlantEvent.EVENTS, write_only=True)
    event_readable = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = PlantEvent
        fields = ['id', 'user_plant_id', 'event_readable', 'event', 'desctiption', 'event_date']

    def get_event_readable(self, obj):
        return obj.get_event_display()



class UserPlantSerializer(serializers.ModelSerializer):

    plant = PlantSerializer(read_only=True, many=False)
    plant_id = serializers.IntegerField(write_only=True)
    events = serializers.SerializerMethodField(read_only=True)

    def get_events(self, user_plant):
        qs = PlantEvent.objects.filter(user_plant=user_plant)
        return PlantEventSerializer(qs, many=True, read_only=True).data

    class Meta:
        model = UserPlant
        fields = ['id', 'name', 'plant', 'plant_id', 'events']