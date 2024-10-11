from django import forms
from .models import MaintenanceSpeciesList

class MaintenanceSpeciesListForm(forms.ModelForm):
    class Meta:
        model = MaintenanceSpeciesList
        fields = [
            'active',  # Checkbox voor actief/inactief
            'nl_name',  # Nederlandse naam
            'name',  # Engelse naam
            'latin_name',  # Latijnse naam
            'WoRMS',  # WoRMS nummer
            'pauly_trophic_level',  # Pauly Trophic Level
            'var_x',  # Vrij tekstveld
            'fishflag',  # Checkbox voor vissoorten
            'collecting_per_week',  # Aantal keer verzamelen per week
            'always_collecting'  # Checkbox voor altijd verzamelen
        ]
        widgets = {
            'active': forms.CheckboxInput(),  # Widget voor de checkbox
            'fishflag': forms.CheckboxInput(),  # Widget voor fishflag checkbox
            'always_collecting': forms.CheckboxInput(),  # Widget voor always_collecting checkbox
        }
