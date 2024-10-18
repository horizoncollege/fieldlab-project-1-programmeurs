from django.db import models

class MaintenanceSpeciesList(models.Model):
    ## model layout pre-update:
    # 
    # active = models.BooleanField(default=True)
    # nl_name = models.CharField(max_length=255)
    # name = models.CharField(max_length=255)
    # latin_name = models.CharField(max_length=255)
    # WoRMS = models.CharField(max_length=255)
    # pauly_trophic_level = models.DecimalField(max_digits=4, decimal_places=2)
    # var_x = models.TextField(blank=True, null=True)
    # fishflag = models.BooleanField(default=False)
    # collecting_per_week = models.IntegerField()
    # always_collecting = models.BooleanField(default=False)
    
    ## old database model compatible with sql data from old environment:
    # 
    active = models.BooleanField(default=True)
    nl_name = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    latin_name = models.CharField(max_length=255)
    WoRMS = models.CharField(max_length=255)
    var_x = models.TextField(blank=True, null=True)
    fishflag = models.BooleanField(default=False)
    oldnrmee = models.TextField(blank=True, null=True)
    pauly_trophic_level = models.CharField(max_length=50)
    extraction_date = models.CharField(max_length=50)
    always_collecting = models.BooleanField(default=False)
    indivweek = models.IntegerField()
    collecting_per_week = models.IntegerField()
    
    ## updated model with new values added below ##
    # 
    # active = models.BooleanField(default=True)
    # nl_name = models.CharField(max_length=255)
    # name = models.CharField(max_length=255)
    # latin_name = models.CharField(max_length=255)
    # WoRMS = models.CharField(max_length=255)
    # pauly_trophic_level = models.CharField(max_length=50)
    # var_x = models.TextField(blank=True, null=True)
    # fishflag = models.BooleanField(default=False)
    # collecting_per_week = models.IntegerField()
    # always_collecting = models.BooleanField(default=False)
    ## below are the new values
    # indivweek = models.IntegerField()
    # extraction_date = models.CharField(max_length=50)
    # oldnrmee = models.TextField(blank=True, null=True)
    # speciesid = models.IntegerField()
    
    class Meta:
        db_table = 'maintenance_species_list'

    def __str__(self):
        return self.nl_name
