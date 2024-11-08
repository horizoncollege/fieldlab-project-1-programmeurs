from django.shortcuts import render, redirect, get_object_or_404
from .models import DataCollection, FykeLocations, FishDetails
from datetime import datetime
from .forms import DataCollectionForm
from django.db.models.functions import ExtractYear, ExtractWeek
from math import ceil

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
        form = DataCollectionForm(instance=record)

    # Render the edit form template
    return render(request, 'datacollection/edit_record.html', {
        'form': form,
        # 'record': record,
    })

def biotic(request, pk):
    # Retrieve the specific record from the DataCollection model using the primary key
    record = get_object_or_404(DataCollection.objects.annotate(
        year=ExtractYear('date'),  # Extract year from the date
        week=ExtractWeek('date')    # Extract week from the date
    ), pk=pk)

    return render(request, 'datacollection/biotic.html', {
        'record': record,  # Pass the record to the template
    })
    
# Fishdetails
def fishdetails(request):
    # Extract the year and week from the 'collectdate' field in the database
    data = FishDetails.objects.annotate(
        year=ExtractYear('collectdate'),
        week=ExtractWeek('collectdate')
    )

    # Get distinct years based on the 'collectdate' field
    years = data.values_list('year', flat=True).distinct().order_by('year')
    weeks = []

    # Check if a year filter is applied in the URL
    selected_year = request.GET.get('year')
    selected_week = request.GET.get('week')
    selected_range = request.GET.get('range')
    selected_species = request.GET.get('species')
    
    # Initialize species_data
    species_data = None
    
    # Start with filtering by year
    if selected_year:
        selected_year = int(selected_year)  # Convert to int for comparison
        data = data.filter(year=selected_year)  # Filter data based on extracted year
        
        # Get distinct weeks for the selected year
        weeks = data.values_list('week', flat=True).distinct().order_by('week')

        # If a week filter is applied, filter further by week
        if selected_week:
            selected_week = int(selected_week)  # Convert to int for comparison
            data = data.filter(week=selected_week)
        
        # Retrieve 'collectno' values from the filtered data
        collect_numbers = data.values_list('collectno', flat=True).distinct()

        # Group the collect numbers into ranges (1-5, 6-10, etc.)
        max_collect = max(collect_numbers) if collect_numbers else 0
        range_groups = []
        
        # Generate the range groups dynamically
        for i in range(1, ceil(max_collect / 5) + 1):
            start = (i - 1) * 5 + 1
            end = i * 5
            # Collect numbers in the current range
            range_groups.append({
                'start': start,
                'end': end,
                'collect_in_range': [c for c in collect_numbers if start <= c <= end]
            })

        # Add the all-inclusive range group as the first item
        if collect_numbers:
            min_collect = min(collect_numbers)
            max_collect = max(collect_numbers)
            range_groups.insert(0, {
                'start': min_collect,
                'end': max_collect,
                'collect_in_range': collect_numbers,
                'label': 'All'  # Add a label for easier HTML handling
            })

        # If range filter is applied, filter collect numbers by range
        if selected_range:
            range_start, range_end = map(int, selected_range.split('-'))
            data = data.filter(collectno__gte=range_start, collectno__lte=range_end)
            
            
        if selected_species:
            try:
                species_id = int(selected_species)
                species_data = FishDetails.objects.filter(species=species_id).annotate(
                    year=ExtractYear('collectdate'),
                    week=ExtractWeek('collectdate')
                )
                
                for value in species_data:
                    for field in value.__class__._meta.fields:
                        if getattr(value, field.name) is None:
                            setattr(value, field.name, "")  # Set to empty string if None
                
            except (ValueError, FishDetails.DoesNotExist):
                species_data = None
        
    
    else:
        # If no year is selected, show all records and no week or range filtering
        data = FishDetails.objects.all()
        collect_numbers = []
        range_groups = []
    
    # Create a context dictionary for the sorting values used to sort by year etc.
    context = {
        'data': data,
        'years': years,
        'weeks': weeks,
        'range_groups': range_groups,
        'species_data' : species_data,
        'selected_year': selected_year,
        'selected_week': selected_week,
        'selected_range': selected_range,
        'selected_species' : selected_species,
    }
    
    return render(request, 'fishdetails.html', context)


# Fykelocations
def fykelocations(request):
    # Retrieve all records from the FykeLocations table
    data = FykeLocations.objects.all()  # This gets all entries in the table
    
    return render(request, 'fykelocations.html', {
        'data': data  # Pass the data to the template
    })

def new_location(request):
    return render(request, 'fykelocations/new_location.html')
    
def edit_location(request, pk):
    return render(request, 'fykelocations/edit_location.html')


# Exportdata
def exportdata(request):
    return render(request, 'exportdata.html')