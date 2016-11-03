from django.db import models

from django.db import models


class Communication(models.Model):
    type_of_communication = models.CharField(max_length=200)
    create_on = models.DateTimeField('Date Published')


class Track(models.Model):
    user = models.CharField(max_length=80)
    role = models.CharField(max_length=10)
    state = models.IntegerField(default=0)