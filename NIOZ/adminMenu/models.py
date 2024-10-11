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
    accessTexel = models.IntegerField(max_length=1)
    accessLauwersoog = models.IntegerField(max_length=1)
    fishdata = models.IntegerField(max_length=1)
    deleteRecords = models.IntegerField(max_length=1)
    fishdataExport = models.IntegerField(max_length=1)
    fishdataRecords = models.IntegerField(max_length=1)
    fishdataSource = models.IntegerField(max_length=1)
    fyke = models.IntegerField(max_length=1)
    fykeBioticdata = models.IntegerField(max_length=1)
    fykeDatacollection = models.IntegerField(max_length=1)
    fykeExportdata = models.IntegerField(max_length=1)
    fykeFishDetails = models.IntegerField(max_length=1)
    fykeLocations = models.IntegerField(max_length=1)
    help = models.IntegerField(max_length=1)
    maintenance = models.IntegerField(max_length=1)
    maintenanceFishprogrammes = models.IntegerField(max_length=1)
    maintenanceLocations = models.IntegerField(max_length=1)
    maintenanceSpecies = models.IntegerField(max_length=1)
    manager = models.IntegerField(max_length=1)
    managerUserAccess = models.IntegerField(max_length=1)
    options = models.IntegerField(max_length=1)
    optionsUserSettings = models.IntegerField(max_length=1)


def __str__(self):
        return f'{self.username} {self.active} {self.realName} {self.collectlocation} {self.yearFrom} {self.yearUntil} {self.accessTexel} {self.accessLauwersoog} {self.fishdata} {self.deleteRecords} {self.fishdataExport} {self.fishdataRecords} {self.fishdataSource} {self.fyke} {self.fykeBioticdata}{self.fykeDatacollection} {self.fykeExportdata} {self.fykeFishDetails} {self.fykeLocations} {self.help} {self.maintenance} {self.maintenanceFishprogrammes} {self.maintenanceLocations}{self.maintenanceSpecies} {self.manager} {self.managerUserAccess} {self.options} {self.optionsUserSettings}'