from django.db import models
from django.db.models import Manager

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    count = models.PositiveIntegerField()
    description = models.CharField(max_length=1000, default="You description")

    objects: Manager