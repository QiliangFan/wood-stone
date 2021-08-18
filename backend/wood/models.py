from django.db import models
from django.db.models import Model

# Create your models here.


class Series(Model):

    name = models.CharField(max_length=128, blank=False)
    timestamp = models.IntegerField(blank=False)
    value = models.FloatField(blank=True)
    label = models.SmallIntegerField(blank=True)
    missing = models.SmallIntegerField(blank=True)