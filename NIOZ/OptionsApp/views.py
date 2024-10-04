from django.shortcuts import render

def options_view(request):
    return render(request, 'OptionsApp.html')