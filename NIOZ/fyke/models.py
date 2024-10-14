from django.db import models

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
    
        
# class Fishdetails(models.Model):
#     collectdate = models.DateField()
#     species = models.CharField(max_length=50)