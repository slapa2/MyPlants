from django.contrib.auth.models import User
from rest_framework import serializers

from django.contrib.auth.models import User
from rest_framework.fields import ChoiceField

from apps.plants.models import Plant, UserPlant, PlantEvent


class PlantSerializer(serializers.ModelSerializer):

    class Meta:
        model = Plant
        fields = ['id', 'latin_name', 'polish_name', 'image']


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
    user_plant_id = serializers.IntegerField(write_only=True)
    events = serializers.SerializerMethodField()


    def get_events(self, user_plant):
        qs = PlantEvent.objects.filter(user_plant=user_plant)
        return PlantEventSerializer(qs, many=True, read_only=True).data

    class Meta:
        model = UserPlant
        fields = ['id', 'name','plant',  'user_plant_id', 'events']


