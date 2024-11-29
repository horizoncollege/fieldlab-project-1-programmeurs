from django.contrib import admin
from .models import MaintenanceSpeciesList, FykeLocation, FykeProgramme


# Register de MaintenanceSpeciesList admin
@admin.register(MaintenanceSpeciesList)
class MaintenanceSpeciesListAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'nl_name', 'en_name', 'latin_name', 'active',
        'species_id', 'pauly_trophic_level', 'collecting_per_week'
    )
    list_filter = ('active', 'fishflag', 'always_collecting')
    search_fields = ('nl_name', 'en_name', 'latin_name', 'WoRMS')
    ordering = ('species_id',)
    
    def species_id(self, obj):
        return obj.species_id

# Register de FykeLocation admin
@admin.register(FykeLocation)
class FykeLocationAdmin(admin.ModelAdmin):
    list_display = ('no', 'location', 'comment')
    search_fields = ('location',)
    ordering = ('no',)

# Register de FykeProgramme admin
@admin.register(FykeProgramme)
class FykeProgrammeAdmin(admin.ModelAdmin):
    list_display = ('no', 'programme', 'comment')
    search_fields = ('programme',)
    ordering = ('no',)
    

