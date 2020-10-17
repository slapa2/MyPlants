from datetime import date

from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import DateTimeField

from django_resized import ResizedImageField

class Plant(models.Model):
    latin_name = models.CharField(max_length=200, unique=True)
    polish_name = models.CharField(max_length=200, null=True, blank=True)
    image = ResizedImageField(upload_to='plants_imgs/', null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='plant_created_by')
    updated_at = DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='plant_updated_by')

    class Meta:
        ordering = ['latin_name']

    def __str__(self):
        return f'{self.latin_name} [{self.polish_name}]'
