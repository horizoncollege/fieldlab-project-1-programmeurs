from django.shortcuts import render, redirect
from .models import DataCollection
from datetime import datetime
from .forms import DataCollectionForm
\

# Index
def index(request):
    return render(request, 'index.html')


# DataCollection
def datacollection_view(request):
    data = DataCollection.objects.all()  # Fetch all records
    return render(request, 'datacollection.html', {'data': data})

def new_record_view(request):
    if request.method == 'POST':
        # Get the form data, including the fyke dropdown
        fyke = request.POST.get('fyke')  # Get the value from the custom dropdown
        
        # Create a form instance with the POST data
        form = DataCollectionForm(request.POST)
        
        if form.is_valid():
            # Create the instance and save it
            new_record = form.save(commit=False)  # Don't save to the database yet
            new_record.fyke = fyke               # Set the fyke field from the dropdown
            new_record.save()                     # Now save the instance
            return redirect('datacollection')     # Redirect after successful submission
        else:
            print(form.errors)
    else:
        # Get the current year and week number
        current_year = datetime.now().year
        current_week = datetime.now().isocalendar()[1]  # Get the current week number
        
        # Choose a reference date (e.g., Jan 1 of the current year)
        reference_date = datetime(current_year, 1, 1)  # Change as needed
        
        # Calculate fishingday as the number of days since the reference date
        today = datetime.now()
        fishingday = (today - reference_date).days
        
        version = '3.0'

        # Set the initial values for the form
        form = DataCollectionForm(initial={
            'year': current_year,
            'week': current_week,
            'fishingday': fishingday,
            'version': version,
        })

    # Pass the variables to the template context
    return render(request, 'datacollection/new_record.html', {
        'form': form,
        'current_year': current_year,   # Add this line
        'current_week': current_week,     # Add this line
        'fishingday': fishingday,         # Add this line
    })

# Fishdetails
def fishdetails(request):
    return render(request, 'fishdetails.html')


# Fykelocations
def fykelocations(request):
    return render(request, 'fykelocations.html')


# Exportdata
def exportdata(request):
    return render(request, 'exportdata.html')