from django.shortcuts import render

def admin_menu_view(request):
    return render(request, 'adminMenu/adminMenu.html')

def hardcoded_people_view(request):
#hard coded data for now until database is accessible
    people = [
        {'Username': 'Alice154', 'realName': 'Alice', 'collectlocation': 'Texel (RW) Lauwersoog (RW)', 'yearFrom': 2004, 'yearUntil': '∞'},
        {'Username': 'BobTheMan', 'realName': 'Bob', 'collectlocation': 'Texel (RW) Lauwersoog (RW)', 'yearFrom': 2014, 'yearUntil': '∞'},
        {'Username': 'CharlieTheGoat', 'realName': 'Charlie', 'collectlocation': 'Texel (RW) Lauwersoog (RW)', 'yearFrom': 1997, 'yearUntil': '∞'},
        {'Username': 'Diana372', 'realName': 'Diana', 'collectlocation': 'Texel (RW) Lauwersoog (RW)', 'yearFrom': 2018, 'yearUntil': '∞'},
        {'Username': 'EthanBoy', 'realName': 'Ethan', 'collectlocation': 'Texel (RW) Lauwersoog (RW)', 'yearFrom': 1999, 'yearUntil': '∞'},
    ]

    return render(request, 'adminMenu/adminMenu.html', {'people': people})