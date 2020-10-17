from django.contrib.auth.models import User
from django.db.models import query
from rest_framework import serializers

from django.contrib.auth.models import User
from rest_framework.fields import ChoiceField

from apps.plants.models import Plant


class PlantSerializer(serializers.ModelSerializer):

    class Meta:
        model = Plant
        fields = ['id', 'latin_name', 'polish_name', 'image']
        queryset = Plant.objects.all()


