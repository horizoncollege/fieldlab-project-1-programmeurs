from django.shortcuts import render
from django.shortcuts import redirect
from .models import MaintenanceSpeciesList
from .forms import MaintenanceSpeciesListForm

def index(request):
    return render(request, 'maintenance/index.html')

def species_list(request):
    if request.method == 'POST':
        form = MaintenanceSpeciesListForm(request.POST)
        if form.is_valid():
            form.save()  # Sla de gegevens op in de database
            return redirect('species_list')  # Redirect om dubbele submits te voorkomen
    else:
        form = MaintenanceSpeciesListForm()  # Maak een leeg formulier

    # Haal alle soorten op uit de database
    species = MaintenanceSpeciesList.objects.all()

    # Render de template met zowel het formulier als de lijst met soorten
    return render(request, 'maintenance/species_list.html', {'form': form, 'species': species})


def fishprogrammes(request):
    return render(request, 'maintenance/fishprogrammes.html')

def fishlocations(request):
    return render(request, 'maintenance/fishlocations.html')

def species_list_new(request):
    return render(request, 'maintenance/species_list/species_list_new.html')

