from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from .models import Person

def admin_menu_view(request):
    return render(request, 'adminMenu/adminMenu.html')

def admin_menu_view(request):
    persons = Person.objects.all()
    return render(request, 'adminMenu/adminMenu.html', {'persons': persons})

def adminMenu(request):
    return render(request, 'adminMenu/adminMenu.html')

def admin_menu_user(request):
    return render(request, 'adminMenu/adminMenuUser.html')

