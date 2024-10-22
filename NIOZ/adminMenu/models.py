from django.db import models
from django.core.validators import RegexValidator

class Person(models.Model):
    username = models.CharField(max_length=50)
    active = models.BooleanField(default=True)
    realName = models.CharField(max_length=50)
    collectlocation = models.CharField(max_length=50)
    yearFrom = models.CharField(max_length=10, validators=[RegexValidator(r'^\d+$', 'Only numeric characters are allowed.')])
    yearUntil = models.CharField(max_length=10)
    
    # Remove max_length from IntegerField
    accessTexel = models.IntegerField()
    accessLauwersoog = models.IntegerField()
    fishdata = models.IntegerField()
    deleteRecords = models.IntegerField()
    fishdataExport = models.IntegerField()
    fishdataRecords = models.IntegerField()
    fishdataSource = models.IntegerField()
    fyke = models.IntegerField()
    fykeBioticdata = models.IntegerField()
    fykeDatacollection = models.IntegerField()
    fykeExportdata = models.IntegerField()
    fykeFishDetails = models.IntegerField()
    fykeLocations = models.IntegerField()
    help = models.IntegerField()
    maintenance = models.IntegerField()
    maintenanceFishprogrammes = models.IntegerField()
    maintenanceLocations = models.IntegerField()
    maintenanceSpecies = models.IntegerField()
    manager = models.IntegerField()
    managerUserAccess = models.IntegerField()
    options = models.IntegerField()
    optionsUserSettings = models.IntegerField()

    def __str__(self):
        return f'{self.username} {self.active} {self.realName} {self.collectlocation} {self.yearFrom} {self.yearUntil} {self.accessTexel} {self.accessLauwersoog} {self.fishdata} {self.deleteRecords} {self.fishdataExport} {self.fishdataRecords} {self.fishdataSource} {self.fyke} {self.fykeBioticdata}{self.fykeDatacollection} {self.fykeExportdata} {self.fykeFishDetails} {self.fykeLocations} {self.help} {self.maintenance} {self.maintenanceFishprogrammes} {self.maintenanceLocations}{self.maintenanceSpecies} {self.manager} {self.managerUserAccess} {self.options} {self.optionsUserSettings}'
