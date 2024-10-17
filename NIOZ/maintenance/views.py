from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import MaintenanceSpeciesList
from .forms import MaintenanceSpeciesListForm

def index(request):
    return render(request, 'maintenance/index.html')

def species_list(request):
    sort_field = request.GET.get('sort', 'id')  # Standaard sorteren op 'id'
    sort_order = request.GET.get('order', 'asc')  # Standaard volgorde is 'asc'
    print(sort_order)

    # Controleer of de huidige sortering opnieuw moet worden omgekeerd
    # if request.GET.get('sort') == sort_field:
    if sort_order == 'desc':
            sort_order = 'asc'
    else:
            sort_order = 'desc'
    # else:
        # sort_order = 'asc'  # Reset naar 'asc' als een andere kolom wordt aangeklikt

    # Maak een dynamische queryset op basis van sort_field en sort_order
    species = MaintenanceSpeciesList.objects.all()
    if sort_order == 'asc':
        species = species.order_by(sort_field)
    else:
        species = species.order_by(f'-{sort_field}')

    if request.method == 'POST':
        form = MaintenanceSpeciesListForm(request.POST)
        if form.is_valid():
            form.save()  # Sla de gegevens op in de database
            return redirect('species_list')  # Redirect om dubbele submits te voorkomen
    else:
        form = MaintenanceSpeciesListForm()  # Maak een leeg formulier

    # Voeg de volgende variabelen toe voor gebruik in de template
    context = {
        'form': form,
        'species': species,
        'sort_field': sort_field,
        'sort_order': sort_order,
    }

    return render(request, 'maintenance/species_list.html', context)





def species_edit(request, species_id):
    specie = get_object_or_404(MaintenanceSpeciesList, pk=species_id)
    if request.method == 'POST':
        form = MaintenanceSpeciesListForm(request.POST, instance=specie)
        if form.is_valid():
            form.save()
            return redirect('species_list')  # Redirect naar de lijst na het opslaan
    else:
        form = MaintenanceSpeciesListForm(instance=specie)  # Vul het formulier met de huidige gegevens

    species = MaintenanceSpeciesList.objects.all()

    return render(request, 'maintenance/species_edit.html', {
        'form': form,
        'specie': specie,
        'species': species,
    })

def fishprogrammes(request):
    return render(request, 'maintenance/fishprogrammes.html')

def fishlocations(request):
    return render(request, 'maintenance/fishlocations.html')

def species_detail(request, species_id):
    specie = get_object_or_404(MaintenanceSpeciesList, pk=species_id)
    data = {
        'id': specie.id,
        'active': specie.active,
        'nl_name': specie.nl_name,
        'name': specie.name,
        'latin_name': specie.latin_name,
        'WoRMS': specie.WoRMS,
        'pauly_trophic_level': str(specie.pauly_trophic_level),
        'var_x': specie.var_x,
        'fishflag': specie.fishflag,
        'collecting_per_week': specie.collecting_per_week,
        'always_collecting': specie.always_collecting,
    }
    return JsonResponse(data)
