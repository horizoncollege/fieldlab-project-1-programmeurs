from django import forms
from .models import DataCollection
from django.shortcuts import render, redirect
from django.forms import ModelForm
from .models import CatchLocations

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
            'version',
        ]

        # widgets = {
        #     'date': forms.DateInput(
        #         attrs={
        #             'type': 'date',
        #         },
        #         format='%d/%m/%Y'
        #     ),
            
        #     'time': forms.TimeInput(
        #         attrs={
        #             'type': 'time',
        #         },
        #     )
        # }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Set specific fields to not be required
        for field in [
            'observer', 'tidal_phase', 'salinity', 'temperature',
            'wind_direction', 'wind_speed', 'secchi_depth', 'fu_scale', 'remarks'
        ]:
            self.fields[field].required = False

        # Set initial value for new records
        if not self.instance.pk:  # Check if it's a new instance
            self.fields['remarks'].initial = ""  # Set initial value to empty for new records

class CatchLocationsForm(ModelForm):
    class Meta:
        model = CatchLocations
        fields = ['name', 'type', 'latitude', 'longitude', 'remarks', 'collect_group', 'print_label']