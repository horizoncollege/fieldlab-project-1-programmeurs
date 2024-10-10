from django.shortcuts import render

def index(request):
    return render(request, 'maintenance/index.html')

def species_list(request):
    return render(request, 'maintenance/species_list.html')
def fishprogrammes(request):
    return render(request, 'maintenance/fishprogrammes.html')
def fishlocations(request):
    return render(request, 'maintenance/fishlocations.html')
