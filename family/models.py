from django.db import models

# Create your models here.
class Family(models.Model):
    edad = models.IntegerField()
    nombre = models.CharField(max_length=40)
    nacimiento = models.DateField()


