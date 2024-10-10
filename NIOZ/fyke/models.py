from django.db import models

class DataCollection(models.Model):
    tidal_phase = models.CharField(max_length=50)
    salinity = models.IntegerField()
    temperature = models.IntegerField()
    wind_direction = models.CharField(max_length=10)
    wind_speed = models.IntegerField()
    secchi_depth = models.IntegerField()
    fu_scale = models.CharField(max_length=10)

    date = models.DateField()
    time = models.TimeField()
    year = models.IntegerField()
    week = models.IntegerField()
    fishingday = models.IntegerField()
    fyke = models.CharField(max_length=255)
    duration = models.IntegerField()
    collect = models.IntegerField()
    remarks = models.TextField()
    observer = models.CharField(max_length=255)
    version = models.CharField(max_length=255)

    class Meta:
        db_table = 'fyke_datacollection'  # Set the name to your existing database table

    def __str__(self):
        return f"DataCollection on {self.date} by {self.observer}"
    

from django import forms
from .models import DataCollection

class DataCollectionForm(forms.ModelForm):
    class Meta:
        model = DataCollection
        fields = [
            'tidal_phase', 'salinity', 'temperature',
            'wind_direction', 'wind_speed', 'secchi_depth',
            'fu_scale', 
            'date',
            'time',
            'year',
            'week',
            'fishingday',
            'fyke',
            'duration',
            'collect',
            'remarks',
            'observer',
            'version'
        ]
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),  # Should render as <input type="date">
            # 'time': forms.TimeInput(attrs={'type': 'time'}),   # Should render as <input type="time">
        }