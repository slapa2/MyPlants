from django.shortcuts import render

from rest_framework import viewsets

from .models import Book, PlantBook
from .serializers import BookSerializer, PlantBookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class PlantBookViewSet(viewsets.ModelViewSet):
    queryset = PlantBook.objects.all()
    serializer_class = PlantBookSerializer