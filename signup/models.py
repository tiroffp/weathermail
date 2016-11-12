from django.db import models


# Create your models here.
class City(models.Model):
    name = models.TextField(primary_key=True)
    state = models.TextField()

    class Meta():
        ordering = ['name']


class Subscriber(models.Model):
    email = models.TextField(primary_key=True)
    city = models.ForeignKey(City)
