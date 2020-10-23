from django.contrib.auth.models import User
from django.db.models import query
from rest_framework import serializers

from django.contrib.auth.models import User
from rest_framework.fields import ChoiceField

from apps.plants.models import Plant
from apps.books.serializers import PlantBookSerializer


class PlantSerializer(serializers.HyperlinkedModelSerializer):

    books = PlantBookSerializer(read_only=True, many=True)

    class Meta:
        model = Plant
        fields = ['id', 'url', 'latin_name', 'polish_name', 'image', 'books', ]
        queryset = Plant.objects.all()


