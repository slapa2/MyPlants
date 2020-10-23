from django.db import models
from django.db.models.fields.related import ForeignKey

from django_resized import ResizedImageField

from apps.plants.models import Plant


class Book(models.Model):
    title = models.CharField(max_length=200)
    isbn = models.CharField(max_length=50, null=True, blank=True)
    cover_image = ResizedImageField(upload_to='plants_imgs/', null=True, blank=True)

    def __str__(self):
        return self.title


class PlantBook(models.Model):
    plant = models.ForeignKey(Plant, related_name='books', on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    page = models.PositiveSmallIntegerField()