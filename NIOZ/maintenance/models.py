from django.db import models


class MaintenanceSpeciesList(models.Model):
    id = models.AutoField(primary_key=True)
    species_id = models.IntegerField()
    active = models.BooleanField(default=True)
    nl_name = models.CharField(max_length=255)
    en_name = models.CharField(max_length=255)
    latin_name = models.CharField(max_length=255)
    WoRMS = models.CharField(max_length=255)
    pauly_trophic_level = models.FloatField()
    var_x = models.TextField(blank=True, null=True)
    fishflag = models.BooleanField(default=False)
    collecting_per_week = models.IntegerField()
    always_collecting = models.BooleanField(default=True)

    class Meta:
        db_table = 'maintenance_species_list'
        verbose_name = "Species list"  # Nieuw enkelvoudige naam
        verbose_name_plural = "Species list"  # Nieuw meervoudige naam

    def __str__(self):
        return self.nl_name
    
class FykeLocation(models.Model):
    no = models.AutoField(primary_key=True)  # Auto-incrementing 'no'
    location = models.CharField(max_length=255)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'fyke_locations'
        verbose_name = "Fyke Location"
        verbose_name_plural = "Fyke Locations"

    def __str__(self):
        return f"{self.no} - {self.location}"

class FykeProgramme(models.Model):
    no = models.AutoField(primary_key=True)  # Auto-incrementing 'no'
    programme = models.CharField(max_length=255)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'fyke_programmes'
        verbose_name = "Fyke Programme"
        verbose_name_plural = "Fyke Programmes"

    def __str__(self):
        return f"{self.no} - {self.programme}"



