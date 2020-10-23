from django.db.models import fields
from rest_framework import serializers

from .models import PlantBook, Book
from apps.plants.models import Plant

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'cover_image', ]
        queryset = Book.objects.all()

    def get_queryset(self, request):
        return Book.objects.all()



class PlantBookSerializer(serializers.ModelSerializer):

    plant_id = serializers.PrimaryKeyRelatedField(queryset=Plant.objects.all())
    book_id = serializers.PrimaryKeyRelatedField(queryset=Book.objects.all(), write_only=True)
    book = BookSerializer(read_only=True)

    class Meta:
        model = PlantBook
        fields = ['id', 'book_id', 'plant_id', 'book', 'page', ]
        queryset = PlantBook.objects.all()