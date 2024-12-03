from django.db import models
from django.contrib.auth.models import User

class DataCollection(models.Model):
    tidal_phase = models.CharField(max_length=50, blank=True, null=True)
    salinity = models.IntegerField(blank=True, null=True)
    temperature = models.IntegerField(blank=True, null=True)
    wind_direction = models.CharField(max_length=10, blank=True, null=True)
    wind_speed = models.IntegerField(blank=True, null=True)
    secchi_depth = models.IntegerField(blank=True, null=True)
    fu_scale = models.CharField(max_length=10, blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    observer = models.CharField(max_length=255, blank=True, null=True)
    
    changed_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    last_change = models.DateTimeField(auto_now=True)

    date = models.DateField()
    time = models.TimeField()
    fishingday = models.IntegerField()
    fyke = models.CharField()
    duration = models.IntegerField()
    collect = models.IntegerField()
    version = models.CharField(max_length=255)
    
    FYKE_CHOICES = [
        ('Stuifdijk', 'Stuifdijk'),
        ('Afsluitdijk', 'Afsluitdijk'),
        ('Schanserwaard', 'Schanserwaard'),
        ('Pakeerplaats NIOZ achter', 'Pakeerplaats NIOZ achter'),
        ('Parkeerplaats haven', 'Parkeerplaats haven'),
        ('Texelstroom', 'Texelstroom'),
        ('NIOZ dam', 'NIOZ dam'),
        ('Navicula', 'Navicula'),
        ('Wierbalg', 'Wierbalg'),
        ('WMR-NIOZ otoliths project', 'WMR-NIOZ otoliths project'),
        ('Gat v Stier', 'Gat v Stier'),
        ('HW-prog', 'HW-prog'),
        ('IJhaven Amsterdam', 'IJhaven Amsterdam'),
        ('NA', 'NA'),
        ('NIOZ_Harbour', 'NIOZ_Harbour'),
        ('North Sea', 'North Sea'),
        ('Terschelling', 'Terschelling'),
        ('Texelstroom', 'Texelstroom'),
        ('WaddenSea', 'WaddenSea'),
        ('Texel beach', 'Texel beach'),
        ('Fyke Sieme', 'Fyke Sieme'),
        ('Eems', 'Eems'),
        ('Dooie Hond', 'Dooie Hond'),
        ('Eerste hoofd', 'Eerste hoofd'),
        ('Veerhaven', 'Veerhaven'),
        ('Hors', 'Hors'),
        ('Schanderwaard', 'Schanderwaard'),
        ('Vlettenstelling', 'Vlettenstelling'),
        ('Hoek van de staak', 'Hoek van de staak'),
        ('Onbekend', 'Onbekend'),
        ('Schiermonnikoog', 'Schiermonnikoog'),
        ('Borkumse stenen', 'Borkumse stenen'),
    ]
    
    fyke = models.CharField(max_length=100, choices=FYKE_CHOICES)

    class Meta:
        db_table = 'fyke_datacollection'  # Set the name to your existing database table

    def __str__(self):
        return f"DataCollection on {self.date} by {self.observer}"
    
    def save(self, *args, **kwargs):
        if not self.changed_by and hasattr(self, 'user') and self.user:
            self.changed_by = self.user  # This assumes you're passing the user as part of the save
        super().save(*args, **kwargs)

class FykeLocations(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    remarks = models.CharField(max_length=256)
    collectgroup = models.CharField(max_length=50)
    printlabel = models.CharField(max_length=50)
    
    OPTIONS = [
        ('Texel', 'Texel'),
        ('Lauwersoog', 'Lauwersoog')
    ]
    
    latitude = models.FloatField(choices=OPTIONS)
    longitude = models.FloatField(choices=OPTIONS)
    
    class Meta:
        db_table = 'fyke_fykelocations'  # Set the name to your existing database table
        
    def __str__(self):
        return f"catchlocations"


class FishDetails(models.Model):
    collectdate = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    registrationtime = models.DateTimeField(auto_now=False, auto_now_add=True, blank=True, null=True)
    collectno = models.IntegerField(blank=True, null=True)
    species = models.ForeignKey(
        'maintenance.MaintenanceSpeciesList',
        on_delete=models.CASCADE,  # Use CASCADE or your preferred option
        related_name='data_collections',  # Optional: for reverse lookup
    )
    condition = models.CharField(max_length=50, blank=True, null=True)
    total_length = models.FloatField(blank=True, null=True)
    fork_length = models.FloatField(blank=True, null=True)
    standard_length = models.FloatField(blank=True, null=True)
    fresh_weight = models.FloatField(blank=True, null=True)
    liver_weight = models.FloatField(blank=True, null=True)
    total_wet_mass = models.FloatField(blank=True, null=True)
    stomach_content = models.CharField(max_length=255, blank=True, null=True)
    gonad_mass = models.FloatField(blank=True, null=True)
    sexe = models.CharField(max_length=50, blank=True, null=True)
    ripeness = models.IntegerField(blank=True, null=True)
    otolith = models.CharField(max_length=50, blank=True, null=True)
    isotopeflag = models.IntegerField(blank=True, null=True)
    total_length_frozen = models.FloatField(blank=True, null=True)
    fork_length_frozen = models.FloatField(blank=True, null=True)
    standard_length_frozen = models.FloatField(blank=True, null=True)
    frozen_mass = models.FloatField(blank=True, null=True)
    height = models.FloatField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    rings = models.IntegerField(blank=True, null=True)
    ogew1 = models.CharField(max_length=50, blank=True, null=True)
    ogew2 = models.CharField(max_length=50, blank=True, null=True)
    tissue_type = models.CharField(max_length=50, blank=True, null=True)
    vial = models.CharField(max_length=50, blank=True, null=True)
    dna_sample = models.BooleanField(blank=True, null=True)
    comment = models.TextField(max_length=255, blank=True, null=True)
    micro_plastic = models.BooleanField(blank=True, null=True)
    
    # changed_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    last_change = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'fyke_fishdetails'
    
    def save(self, *args, **kwargs):
        # Normalize floating-point fields
        for field in self._meta.fields:
            value = getattr(self, field.name)

            # Convert empty strings to None
            if value == '':
                setattr(self, field.name, None)
            
            # Convert ',' to '.' for FloatField inputs
            if isinstance(value, str) and ',' in value:
                try:
                    setattr(self, field.name, float(value.replace(',', '.')))
                except ValueError:
                    setattr(self, field.name, None)
                    
        # Automatically set the changed_by and last_change fields
        if not self.changed_by and hasattr(self, 'user') and self.user:
            self.changed_by = self.user  # This assumes you're passing the user as part of the save

        super().save(*args, **kwargs)