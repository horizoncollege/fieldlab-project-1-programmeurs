from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import DataCollection
from datetime import datetime
from .forms import DataCollectionForm
from django.db.models.functions import ExtractYear, ExtractWeek

# Index
def index(request):
    return render(request, 'index.html')


# DataCollection
def datacollection_view(request):
    # Extract the year and week from the 'date' field in the database
    data = DataCollection.objects.annotate(
        year=ExtractYear('date'),  # Extract year from the date
        week=ExtractWeek('date')    # Extract week from the date
    )

    # Get distinct years based on the 'date' field
    years = data.values_list('year', flat=True).distinct().order_by('year')

    # Check if a year filter is applied in the URL
    selected_year = request.GET.get('year')

    # Filter the records by the selected year, if provided
    if selected_year:
        selected_year = int(selected_year)  # Convert to int for comparison
        data = data.filter(year=selected_year)  # Filter data based on extracted year

    return render(request, 'datacollection.html', {
        'data': data,
        'years': years,  # Pass the dynamically calculated years
        'selected_year': selected_year
    })

def new_record_view(request):
    # Initialize variables
    form = DataCollectionForm()  # Initialize an empty form
    reference_date = datetime(1899, 12, 30)  # Set reference date to Dec 30, 1899

    if request.method == 'POST':
        # Get the form data, including the fyke dropdown and date
        fyke = request.POST.get('fyke')  # Get the value from the custom dropdown
        date_input = request.POST.get('date')  # Get the date input from the form
        observer = request.POST.get('observer')  # Get the observer input

        # Create a form instance with the POST data
        form = DataCollectionForm(request.POST)

        if form.is_valid():
            # Create the record but do not save it yet
            new_record = form.save(commit=False)

            # If a date is provided, extract the year and week
            if date_input:
                selected_date = datetime.strptime(date_input, '%Y-%m-%d')  # Parse the date input
                new_record.year = selected_date.year  # Extract year from date
                new_record.week = selected_date.isocalendar()[1]  # Extract ISO week number from date
                
                # Calculate fishingday based on the entered date
                new_record.fishingday = (selected_date - reference_date).days  # Calculate fishing days from reference date
            else:
                # Fallback to current date values if no date is provided
                today = datetime.now()
                new_record.year = today.year
                new_record.week = today.isocalendar()[1]
                new_record.fishingday = (today - reference_date).days  # Calculate fishing days from reference date
                
            new_record.fyke = fyke  # Set the fyke field from the dropdown
        
            if observer:  # Only set if observer is not empty
                new_record.observer = observer
            else:
                new_record.observer = ''  # Explicitly set to empty if no input

            new_record.save()  # Save the instance to the database
            return redirect('datacollection')  # Redirect after successful submission
        else:
            print(form.errors)

    else:
        # For GET request, initialize default form values (no more year/week since it's derived from date)
        today = datetime.now()
        
        # Calculate fishingday based on the current date
        fishingday = (today - reference_date).days  # Calculate fishing days from reference date

        # Set the initial values for the form
        form = DataCollectionForm(initial={
            'fishingday': fishingday,
            # 'version': '3.0',  # Set the version (if it's always static)
        })

    # Pass the variables to the template context
    return render(request, 'datacollection/new_record.html', {
        'form': form,
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
    # Extract the year and week from the 'date' field in the database
    data = DataCollection.objects.annotate(
        year=ExtractYear('date'),
        week=ExtractWeek('date')
    )

    # Get distinct years based on the 'date' field
    years = data.values_list('year', flat=True).distinct().order_by('year')

    # Check if a year filter is applied in the URL
    selected_year = request.GET.get('year')
    selected_week = request.GET.get('week')

    # Start with filtering by year
    if selected_year:
        selected_year = int(selected_year)  # Convert to int for comparison
        data = data.filter(year=selected_year)  # Filter data based on extracted year
        
        weeks = data.values_list('week', flat=True).distinct().order_by('week')
        
        # If a week filter is applied, filter further by week
        if selected_week:
            selected_week = int(selected_week)  # Convert to int for comparison
            data = data.filter(week=selected_week)
    else:
        # If no year is selected, show all records and no week filtering
        data = DataCollection.objects.all()
        weeks = []

    return render(request, 'fishdetails.html', {
        'data': data,
        'years': years,
        'selected_year': selected_year,
        'selected_week': selected_week,
        'weeks': weeks,
    })


# Fykelocations
def fykelocations(request):
    return render(request, 'fykelocations.html')


# Exportdata
def exportdata(request):
    return render(request, 'exportdata.html')