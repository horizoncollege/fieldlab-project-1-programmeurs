from django.shortcuts import render

def index(request):
    return render(request, 'fyke/index.html')

def datacollection(request):
    return render(request, 'fyke/datacollection.html')
def fishdetails(request):
    return render(request, 'fyke/fishdetails.html')
def fykelocations(request):
    return render(request, 'fyke/fykelocations.html')
def exportdata(request):
    return render(request, 'fyke/exportdata.html')