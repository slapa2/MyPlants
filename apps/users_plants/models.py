from datetime import date

from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import DateTimeField

from apps.plants.models import Plant

class UserPlant(models.Model):
    plant = models.ForeignKey(Plant, on_delete=models.SET_NULL, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.plant.poish_name} [{self.name}]'


class PlantEvent(models.Model):

    EVENTS = (
        ('watering', 'podlewanie'),
        ('fertilization', 'nawożenie'),
        ('transplantation', 'przesadzanie'),
        ('other', 'inne'),
    )

    event = models.CharField(max_length=200, choices=EVENTS)
    desctiption = models.TextField(null=True, blank=True)
    event_date = models.DateField(default=date.today)
    user_plant = models.ForeignKey(UserPlant, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.enent_date} [{self.name}]'

    class Meta:
        ordering = ['event_date']