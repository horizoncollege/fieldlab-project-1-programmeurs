from django.shortcuts import render
from django.db import models
from django.core.validators import RegexValidator

class Person(models.Model):
    username = models.CharField(max_length=50)
    active = models.BooleanField(default=True)
    realName = models.CharField(max_length=50)
    collectlocation = models.CharField(max_length=50)
    yearFrom = models.CharField(max_length=10, validators=[RegexValidator(r'^\d+$', 'Only numeric characters are allowed.')])
    yearUntil = models.CharField(max_length=10)

def __str__(self):
        return f'{self.username} {self.active} {self.realName} {self.collectlocation} {self.yearFrom} {self.yearUntil}'