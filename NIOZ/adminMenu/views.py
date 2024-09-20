from django.shortcuts import render

def admin_menu_view(request):
    return render(request, 'adminMenu/adminMenu.html')
