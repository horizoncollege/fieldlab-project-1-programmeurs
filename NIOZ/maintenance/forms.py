from django import forms
from .models import MaintenanceSpeciesList

class MaintenanceSpeciesListForm(forms.ModelForm):
    class Meta:
        model = MaintenanceSpeciesList
        fields = [
            'species_id',  
            'active',  # Checkbox voor actief/inactief
            'nl_name',  # Nederlandse naam
            'en_name',  # Engelse naam
            'latin_name',  # Latijnse naam
            'WoRMS',  # WoRMS nummer
            'pauly_trophic_level',  # Pauly Trophic Level
            'var_x',  # Vrij tekstveld
            'fishflag',  # Checkbox voor vissoorten
            'collecting_per_week',  # Aantal keer verzamelen per week
            'always_collecting'  # Checkbox voor altijd verzamelen
        ]
        widgets = {
            'species_id': forms.NumberInput(), 
            'active': forms.CheckboxInput(),  # Widget voor de checkbox
            'fishflag': forms.CheckboxInput(),  # Widget voor fishflag checkbox
            'always_collecting': forms.CheckboxInput(),  # Widget voor always_collecting checkbox
            'nl_name': forms.TextInput(attrs={'placeholder': 'Voer de Nederlandse naam in'}),
            'en_name': forms.TextInput(attrs={'placeholder': 'Voer de Engelse naam in'}),
            'latin_name': forms.TextInput(attrs={'placeholder': 'Voer de Latijnse naam in'}),
            'WoRMS': forms.TextInput(attrs={'placeholder': 'Voer het WoRMS nummer in'}),
            'pauly_trophic_level': forms.NumberInput(attrs={'placeholder': 'Voer het Pauly Trophic Level in'}),
            'var_x': forms.Textarea(attrs={'placeholder': 'Voer hier extra informatie in', 'rows': 3}),
            'collecting_per_week': forms.NumberInput(attrs={'placeholder': 'Voer het aantal verzamelingen per week in'}),
        }
