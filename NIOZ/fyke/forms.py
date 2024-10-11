from django import forms
from .models import DataCollection

class DataCollectionForm(forms.ModelForm):
    class Meta:
        model = DataCollection
        fields = [
            'tidal_phase', 'salinity', 'temperature',
            'wind_direction', 'wind_speed', 'secchi_depth',
            'fu_scale', 'date', 'time', 'year', 'week', 
            'fishingday', 'fyke', 'duration', 'collect', 
            'remarks', 'observer', 'version'
        ]
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),  # Should render as <input type="date">
        }
