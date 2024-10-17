from django.db import models

class MaintenanceSpeciesList(models.Model):
    active = models.BooleanField(default=True)
    nl_name = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    latin_name = models.CharField(max_length=255)
    WoRMS = models.CharField(max_length=255)
    pauly_trophic_level = models.DecimalField(max_digits=4, decimal_places=2)
    var_x = models.TextField(blank=True, null=True)
    fishflag = models.BooleanField(default=False)
    collecting_per_week = models.IntegerField()
    always_collecting = models.BooleanField(default=False)

    class Meta:
        db_table = 'maintenance_species_list'

    def __str__(self):
        return self.nl_name
