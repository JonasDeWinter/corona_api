from django.db import models

class Coronagevallen(models.Model):
    land = models.CharField(max_length=50)
    aantalInwoners = models.CharField(max_length=50)
    positievegevallen = models.CharField(max_length=50, default='geen')

