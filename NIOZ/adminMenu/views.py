from django.shortcuts import render, get_object_or_404, redirect
from .models import Person
from django.contrib.auth.forms import UserCreationForm
from .forms import PersonForm

def admin_menu_view(request):
    return render(request, 'adminMenu/adminMenu.html')

def admin_menu_view(request):
    persons = Person.objects.all()
    return render(request, 'adminMenu/adminMenu.html', {'persons': persons})


def adminMenu(request):
    return render(request, 'adminMenu/adminMenu.html')

def admin_menu_new_user(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('adminMenu')
    else:
        form = PersonForm()

    return render(request, 'adminMenu/adminMenuNewUser.html', {'form': form})

def admin_menu_user(request, pk):
    record = get_object_or_404(Person, pk=pk)

    if request.method == 'POST':
        access_texel_value = request.POST.get('accessTexel')
        access_lauwersoog_value = request.POST.get('accessLauwersoog')
        fish_data_value = request.POST.get('fishdata')
        delete_records_value = request.POST.get('deleteRecords')
        fish_data_export_value = request.POST.get('fishdataExport')
        fish_data_records_value = request.POST.get('fishdataRecords')
        fish_data_source_value = request.POST.get('fishdataSource')
        fyke_value = request.POST.get('fyke')
        fyke_biotic_data_value = request.POST.get('fykeBioticdata')
        fyke_datacollection_value = request.POST.get('fykeDatacollection')
        fyke_export_data_value = request.POST.get('fykeExportdata')
        fyke_fish_details_value = request.POST.get('fykeFishDetails')
        fyke_locations_value = request.POST.get('fykeLocations')
        help_value = request.POST.get('help')
        maintenance_value = request.POST.get('maintenance')
        maintenance_fish_programmes_value = request.POST.get('maintenanceFishprogrammes')
        maintenance_locations_value = request.POST.get('maintenanceLocations')
        maintenance_species_value = request.POST.get('maintenanceSpecies')
        manager_value = request.POST.get('manager')
        manager_user_access_value = request.POST.get('managerUserAccess')
        options_value = request.POST.get('options')
        options_user_settings_value = request.POST.get('optionsUserSettings')

        if access_texel_value:  # Check if a value was selected
            record.accessTexel = int(access_texel_value)

        if access_lauwersoog_value:
            record.accessLauwersoog = int(access_lauwersoog_value)

        if fish_data_value:
            record.fishdata = int(fish_data_value)

        if delete_records_value:
            record.deleteRecords = int(delete_records_value)

        if fish_data_export_value:
            record.fishdataExport = int(fish_data_export_value)

        if fish_data_records_value:
            record.fishdataRecords = int(fish_data_records_value)

        if fish_data_source_value:
            record.fishdataSource = int(fish_data_source_value)

        if fyke_value:
            record.fyke = int(fyke_value)

        if fyke_biotic_data_value:
            record.fykeBioticdata = int(fyke_biotic_data_value)

        if fyke_datacollection_value:
            record.fykeDatacollection = int(fyke_datacollection_value)

        if fyke_export_data_value:
            record.fykeExportdata = int(fyke_export_data_value)

        if fyke_fish_details_value:
            record.fykeFishDetails = int(fyke_fish_details_value)

        if fyke_locations_value:
            record.fykeLocations = int(fyke_locations_value)

        if help_value:
            record.help = int(help_value)

        if maintenance_value:
            record.maintenance = int(maintenance_value)

        if maintenance_fish_programmes_value:
            record.maintenanceFishprogrammes = int(maintenance_fish_programmes_value)

        if maintenance_locations_value:
            record.maintenanceLocations = int(maintenance_locations_value)

        if maintenance_species_value:
            record.maintenanceSpecies = int(maintenance_species_value)

        if manager_value:
            record.manager = int(manager_value)

        if manager_user_access_value:
            record.managerUserAccess = int(manager_user_access_value)

        if options_value:
            record.options = int(options_value)

        if options_user_settings_value:
            record.optionsUserSettings = int(options_user_settings_value)
            # slaat de data op in de database
            record.save()
    
    return render(request, 'adminMenu/adminMenuUser.html', {
        'record': record,
    })