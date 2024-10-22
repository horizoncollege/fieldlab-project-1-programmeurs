from django.shortcuts import render
from django.db import models
from django.core.validators import RegexValidator

class Person(models.Model):
    username = models.CharField(max_length=50)
    active = models.BooleanField(default=True)
    realName = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    collectlocation = models.CharField(max_length=100, default="Texel (RW) Lauwersoog (RW)")
    yearFrom = models.CharField(max_length=10, validators=[RegexValidator(r'^\d+$', 'Only numeric characters are allowed.')])
    yearUntil = models.CharField(max_length=10)
    accessTexel = models.IntegerField(default=3)
    accessLauwersoog = models.IntegerField(default=3)
    fishdata = models.IntegerField(default=3)
    deleteRecords = models.IntegerField(default=3)
    fishdataExport = models.IntegerField(default=3)
    fishdataRecords = models.IntegerField(default=3)
    fishdataSource = models.IntegerField(default=3)
    fyke = models.IntegerField(default=3)
    fykeBioticdata = models.IntegerField(default=3)
    fykeDatacollection = models.IntegerField(default=3)
    fykeExportdata = models.IntegerField(default=3)
    fykeFishDetails = models.IntegerField(default=3)
    fykeLocations = models.IntegerField(default=3)
    help = models.IntegerField(default=3)
    maintenance = models.IntegerField(default=3)
    maintenanceFishprogrammes = models.IntegerField(default=3)
    maintenanceLocations = models.IntegerField(default=3)
    maintenanceSpecies = models.IntegerField(default=3)
    manager = models.IntegerField(default=3)
    managerUserAccess = models.IntegerField(default=3)
    options = models.IntegerField(default=3)
    optionsUserSettings = models.IntegerField(default=3)


def __str__(self):
        return f'{self.username} {self.active} {self.realName} {self.password} {self.collectlocation} {self.yearFrom} {self.yearUntil} {self.accessTexel} {self.accessLauwersoog} {self.fishdata} {self.deleteRecords} {self.fishdataExport} {self.fishdataRecords} {self.fishdataSource} {self.fyke} {self.fykeBioticdata}{self.fykeDatacollection} {self.fykeExportdata} {self.fykeFishDetails} {self.fykeLocations} {self.help} {self.maintenance} {self.maintenanceFishprogrammes} {self.maintenanceLocations}{self.maintenanceSpecies} {self.manager} {self.managerUserAccess} {self.options} {self.optionsUserSettings}'

class Meta:
      db_table = 'adminmenu_person'