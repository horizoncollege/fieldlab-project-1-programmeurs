from django.shortcuts import render
from .models import Person

def admin_menu_view(request):
    return render(request, 'adminMenu/adminMenu.html')

def people_list(request):
    people = Person.objects.all()
    return render(request, 'adminMenu/adminMenu.html', {'people': people})