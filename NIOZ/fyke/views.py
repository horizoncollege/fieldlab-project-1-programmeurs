from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import DataCollection
from datetime import datetime
from .forms import DataCollectionForm
\

# Index
def index(request):
    return render(request, 'index.html')


# DataCollection
def datacollection_view(request):
    # Get the distinct years from the records
    years = DataCollection.objects.values_list('year', flat=True).distinct().order_by('year')

    # Check if a year filter is applied in the URL
    selected_year = request.GET.get('year')

    # Convert selected_year to an integer for comparison
    if selected_year:
        selected_year = int(selected_year)  # Convert to int for comparison
        # Filter the records by the selected year
        data = DataCollection.objects.filter(year=selected_year)
    else:
        # If no filter is applied, show all records
        data = DataCollection.objects.all()

    return render(request, 'datacollection.html', {
        'data': data,
        'years': years,
        'selected_year': selected_year
    })

def new_record_view(request):
    if request.method == 'POST':
        # Get the form data, including the fyke dropdown and date
        fyke = request.POST.get('fyke')  # Get the value from the custom dropdown
        date_input = request.POST.get('date')  # Get the date input

        # Create a form instance with the POST data
        form = DataCollectionForm(request.POST)
        
        if form.is_valid():
            # Extract the year from the date if it's provided
            if date_input:
                selected_date = datetime.strptime(date_input, '%Y-%m-%d')  # Adjust format if needed
                new_record = form.save(commit=False)  # Don't save to the database yet
                new_record.year = selected_date.year  # Set the year from the selected date
            else:
                new_record = form.save(commit=False)  # Don't save to the database yet
                new_record.year = datetime.now().year  # Fallback to current year if no date is provided
            
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
        'current_year': current_year,
        'current_week': current_week,
        'fishingday': fishingday,
    })
    
def edit_record_view(request, pk):
    # Retrieve the record from the database or return 404 if it doesn't exist
    record = get_object_or_404(DataCollection, pk=pk)
    
    if request.method == 'POST':
        form = DataCollectionForm(request.POST, instance=record)  # Bind the form with the existing record
        if form.is_valid():
            form.save()  # Save the updated record
            return redirect('datacollection')  # Redirect after successful edit
        else:
            print(form.errors)
    else:
        form = DataCollectionForm(instance=record)  # Pre-fill the form with the existing record

    # Render the edit form template
    return render(request, 'datacollection/edit_record.html', {'form': form, 'record': record})


# Fishdetails
def fishdetails(request):
    return render(request, 'fishdetails.html')


# Fykelocations
def fykelocations(request):
    return render(request, 'fykelocations.html')


# Exportdata
def exportdata(request):
    return render(request, 'exportdata.html')