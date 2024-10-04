from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from .models import Person

def admin_menu_view(request):
    return render(request, 'adminMenu/adminMenu.html')

def people_list(request):
    persons = Person.objects.all()
    return render(request, 'adminMenu/adminMenu.html', {'persons': persons})