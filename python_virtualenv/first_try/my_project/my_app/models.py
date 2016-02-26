from __future__ import unicode_literals

from django.db import models

# Create your models here.

from django.db import models
 
class Person(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=16)

    def __unicode__(self):
        return self.name

