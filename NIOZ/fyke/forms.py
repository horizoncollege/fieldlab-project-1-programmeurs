from django import forms
from .models import DataCollection

class DataCollectionForm(forms.ModelForm):
    class Meta:
        model = DataCollection
        fields = [
            'tidal_phase',
            'salinity',
            'temperature',
            'wind_direction',
            'wind_speed',
            'secchi_depth',
            'fu_scale',
            'date',
            'time',
            'fishingday',
            'fyke',
            'duration',
            'collect', 
            'remarks',
            'observer',
            'version'
        ]
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),  # Should render as <input type="date">
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Set specific fields to not be required
        self.fields['observer'].required = False
        self.fields['tidal_phase'].required = False
        self.fields['salinity'].required = False
        self.fields['temperature'].required = False
        self.fields['wind_direction'].required = False
        self.fields['wind_speed'].required = False
        self.fields['secchi_depth'].required = False
        self.fields['fu_scale'].required = False
        self.fields['remarks'].required = False
        
        if not self.instance.pk:  # Check if it's a new instance
            self.fields['remarks'].initial = ""  # Set initial value to empty for new records
