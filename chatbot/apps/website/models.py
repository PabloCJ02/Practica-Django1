from django.db import models


# Create your models here.

class Comida(models.Model):
    nombre = models.CharField(max_length=100)