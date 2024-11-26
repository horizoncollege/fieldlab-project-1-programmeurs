from django.shortcuts import render, redirect, get_object_or_404
from .models import DataCollection, FykeLocations, FishDetails
from datetime import datetime
from .forms import DataCollectionForm
from django.db.models.functions import ExtractYear, ExtractWeek
from math import ceil
from urllib.parse import urlencode
from django.http import JsonResponse
from maintenance.models import MaintenanceSpeciesList

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
    reference_date = datetime(1899, 12, 30).date()  # Use .date() to get just the date part
    
    now = datetime.now()  # Get the full datetime object for date and time
    formatted_date = now.strftime('%d/%m/%Y')  # Format date as dd/mm/yyyy
    current_time = now.strftime('%H:%M')  # Format time as HH:mm (24-hour format)

    # Calculate the initial fishingday (number of days since the reference date)
    today = datetime.now().date()  # Ensure it's a date object
    fishingday = (today - reference_date).days

    # Get the last record (previous entry) to calculate the duration
    last_record = DataCollection.objects.order_by('-date', '-time').first()  # Get the most recent record

    if last_record:
        # Combine last record's date and time to create a datetime object
        last_datetime = datetime.combine(last_record.date, last_record.time)
        # Calculate the time difference between now and the last record's timestamp
        time_difference = now - last_datetime
        # Convert the difference to hours, round to the nearest whole number
        duration = round(time_difference.total_seconds() / 3600)  # No decimal places, rounding to the nearest hour
    else:
        # If there is no previous record, set the duration to 0
        duration = 0

    # Initialize the form with initial values
    form = DataCollectionForm(initial={
        'fishingday': fishingday,
        'duration': duration,  # Set the initial value of duration
    })

    if request.method == 'POST':
        form = DataCollectionForm(request.POST)
        
        if form.is_valid():
            # Save the form but do not commit yet
            new_record = form.save(commit=False)

            # Get the selected date and calculate derived fields
            date_input = form.cleaned_data.get('date')  # Use cleaned_data to get the parsed date
            if date_input:
                new_record.year = date_input.year
                new_record.week = date_input.isocalendar()[1]
                new_record.fishingday = (date_input - reference_date).days
            else:
                # Default to the current date if no date is provided
                new_record.year = today.year
                new_record.week = today.isocalendar()[1]
                new_record.fishingday = fishingday

            # Save the record to the database
            new_record.save()

            # Redirect after successful submission
            return redirect('datacollection')
        else:
            # Log errors for debugging
            print(form.errors)

    return render(request, 'datacollection/new_record.html', {
        'fishingday': fishingday,
        'form': form,
        'current_date': formatted_date,
        'current_time': current_time,  # Pass formatted time to template
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
        week=ExtractWeek('collectdate'))
    
    # Get distinct years based on the 'collectdate' field
    years = data.values_list('year', flat=True).distinct().order_by('year')
    weeks = []

    # Check if a year filter is applied in the URL
    selected_year = request.GET.get('year')
    selected_week = request.GET.get('week')
    selected_range = request.GET.get('range')
    selected_species = request.GET.get('species')
    
    # Initialize variables for later use
    species_data = None
    species_list_data = None

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
            # Split the range into start and end values
            range_start, range_end = map(int, selected_range.split('-'))

            # Filter the data based on collectno range
            data = data.filter(collectno__gte=range_start, collectno__lte=range_end)

            # Loop through the data and add the species' nl_name based on the species id
            for record in data:
                species_id = record.species  # Get species ID from the data
                
                species_id = int(species_id) + 1
        
                # Query the species_list table to retrieve the species name (nl_name)
                try:
                    species = MaintenanceSpeciesList.objects.get(id=species_id)
                    record.nl_name = species.nl_name  # Add nl_name to the record
                except MaintenanceSpeciesList.DoesNotExist:
                    record.nl_name = "Unknown species"  # Handle case where species ID is not found
        
        if selected_species:
            try:
                species_id = int(selected_species)  # Get the species ID from the selected_species value
        
                # Retrieve species data for the given species_id
                species_data = FishDetails.objects.filter(species=species_id).annotate(
                    year=ExtractYear('collectdate'),
                    week=ExtractWeek('collectdate')
                )
        
                # Loop through the species_data to add the nl_name for each record
                for value in species_data:
                    # Check if any field is None and set it to an empty string
                    for field in value.__class__._meta.fields:
                        if getattr(value, field.name) is None:
                            setattr(value, field.name, "")  # Set to empty string if None

                    # Retrieve the species nl_name based on the species ID
                    try:
                        # Get the species from the MaintenanceSpeciesList table using species_id
                        species = MaintenanceSpeciesList.objects.get(id=species_id + 1)  # Increment ID as required
                        value.nl_name = species.nl_name  # Add nl_name to the record
                    except MaintenanceSpeciesList.DoesNotExist:
                        value.nl_name = "Unknown species"  # Handle case where species ID is not found
        
            except (ValueError, FishDetails.DoesNotExist):
                species_data = None

    else:
        # If no year is selected, show all records and no week or range filtering
        data = FishDetails.objects.all()
        collect_numbers = []
        range_groups = []
    
    # Handle the form submission
    if request.method == 'POST':
        # Get the fish_id from the POST data
        fish_id = request.POST.get('fish_id')
    
        # Retrieve the FishDetails object or raise a 404 if it doesn't exist
        fish = get_object_or_404(FishDetails, id=fish_id)

        # Define the fields that need to be updated
        fields_to_update = [
            'species', 'condition', 'total_length', 'fork_length', 'standard_length',
            'fresh_weight', 'total_wet_mass', 'stomach_content', 'gonad_mass',
            'sexe', 'ripeness', 'otolith', 'total_length_frozen', 'fork_length_frozen',
            'standard_length_frozen', 'frozen_mass', 'height', 'age', 'rings',
            'ogew1', 'ogew2', 'tissue_type', 'vial', 'comment'
        ]
    
        # Update the fields dynamically
        for field in fields_to_update:
            value = request.POST.get(field, getattr(fish, field))
            setattr(fish, field, value)
    
        # Special handling for boolean fields
        fish.dna_sample = 'dna_sample' in request.POST
        fish.micro_plastic = 'micro_plastic' in request.POST

        # Save the updated fish object
        fish.save()

        # Build the redirect URL with existing query parameters
        current_url = request.path
        query_params = request.GET.copy()  # Get the current query parameters
    
        # Add the updated species value to the query parameters
        updated_species = request.POST.get('species')  # Get the new species value
        if updated_species:
            query_params['species'] = updated_species  # Add or update the species in the query params

        # Redirect to the current URL with the updated query parameters
        return redirect(f'{current_url}?{urlencode(query_params)}')
        
    # Create a context dictionary for the sorting values used to sort by year etc.
    context = {
        'data': data,
        'years': years,
        'weeks': weeks,
        'range_groups': range_groups,
        'species_data' : species_data,
        'species_list_data' : species_list_data,
        'selected_year': selected_year,
        'selected_week': selected_week,
        'selected_range': selected_range,
        'selected_species' : selected_species,
    }
    
    return render(request, 'fishdetails.html', context)

def species_search(request):
    query = request.GET.get('q', '')
    if query:
        # If the query is a number, search by id (id = speciesid + 1)
        if query.isdigit():
            # Convert the query to an integer (assuming it's the speciesid)
            speciesid = int(query)
            # Search by id (speciesid + 1)
            results = MaintenanceSpeciesList.objects.filter(id=speciesid + 1)[:10]  # Search by ID
        else:
            # Search by 'nl_name' if it's not a number
            results = MaintenanceSpeciesList.objects.filter(nl_name__icontains=query)[:10]
        
        # Return the name and the adjusted id (which is speciesid + 1)
        results_data = [{'name': species.nl_name, 'id': species.id} for species in results]
    else:
        results_data = []

    return JsonResponse({'results': results_data})

# Catchlocations
def catchlocations(request):
    # Retrieve all records from the FykeLocations table
    data = FykeLocations.objects.all()  # This gets all entries in the table
    
    return render(request, 'catchlocations.html', {
        'data': data  # Pass the data to the template
    })

def new_location(request):
    return render(request, 'catchlocations/new_location.html')
    
def edit_location(request, pk):
    return render(request, 'catchlocations/edit_location.html')


# Exportdata
def exportdata(request):
    return render(request, 'exportdata.html')