from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class ProductModel(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=100,unique=True)
    price = models.FloatField()
    desc = models.CharField(max_length=200)
    image = models.ImageField(blank=True,upload_to='images')