from django.shortcuts import render, get_object_or_404, redirect
from .models import Person
from .forms import PersonForm
from django.http import JsonResponse

def admin_menu_view(request):
    return render(request, 'adminMenu/adminMenu.html')

def admin_menu_view(request):
    if request.method == 'POST':
        # Get the person ID and active state from the request
        person_id = request.POST.get('person_id')
        active_state = request.POST.get('active') == 'true'  # Convert to boolean

        # Update the active field for the specific person
        try:
            person = Person.objects.get(id=person_id)
            person.active = active_state
            person.save()
            return JsonResponse({'status': 'success'})  # Return success response
        except Person.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Person not found'})

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
        fields = [
            'accessTexel', 'accessLauwersoog', 'fishdata', 'deleteRecords', 'fishdataExport', 
            'fishdataRecords', 'fishdataSource', 'fyke', 'fykeBioticdata', 'fykeDatacollection', 
            'fykeExportdata', 'fykeFishDetails', 'fykeLocations', 'help', 'maintenance', 
            'maintenanceFishprogrammes', 'maintenanceLocations', 'maintenanceSpecies', 'manager', 
            'managerUserAccess', 'options', 'optionsUserSettings'
        ]
        
        for field in fields:
            value = request.POST.get(field)
            if value:
                setattr(record, field, int(value))

        record.save()  # Save the data to the database

    return render(request, 'adminMenu/adminMenuUser.html', {'record': record})