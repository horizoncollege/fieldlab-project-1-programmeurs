from django.shortcuts import render, get_object_or_404, redirect
from .models import Person
from .forms import CustomUserCreationForm
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth.models import User


# Index
def index(request):
    return render(request, 'index_adminmenu.html')

def users_view(request):
    return render(request, 'adminMenu/adminMenu.html')

def users_view(request):
    if request.method == 'POST':
        # Get the person ID and active state from the request
        person_id = request.POST.get('person_id')
        active_state = request.POST.get('active') == 'true'  # Convert to boolean

        # Update the active field in the auth_user table (is_active) for the specific user
        try:
            # Get the Person object to find the associated User
            person = Person.objects.get(id=person_id)
            user = person.user  # Access the related User object
            
            # Update the is_active field in the User model
            user.is_active = active_state
            user.save()  # Save the changes to the User object

            return JsonResponse({'status': 'success'})  # Return success response
        except Person.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Person not found'})

    # If it's a GET request, fetch all persons and their associated users
    persons = Person.objects.all()
    return render(request, 'adminMenu/adminMenu.html', {'persons': persons})


def adminMenu(request):
    return render(request, 'adminMenu/adminMenu.html')


def new_user(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Person.objects.create(
                user=user,
                realName=request.POST.get('realName', ''),
                collectlocation="Texel (RW) Lauwersoog (RW)",
                # Add any other fields you want to pass to Person
            )

            messages.success(request, "User and associated profile created successfully!")
            return redirect('login')  # Redirect to a login page or another view after creation
    else:
        form = CustomUserCreationForm()

    return render(request, 'adminMenu/new_user.html', {'form': form})

def userinfo_view(request, pk):
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

    return render(request, 'adminMenu/user.html', {'record': record})