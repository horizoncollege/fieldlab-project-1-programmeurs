from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

# Alleen ingelogde gebruikers kunnen deze pagina zien
@login_required
def home(request):
    return render(request, 'home.html')

# Verwerkt het inlogformulier
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()  # Haalt de gebruiker op
            login(request, user)  # Logt de gebruiker in
            return redirect('home')  # Stuur door naar de startpagina
    else:
        form = AuthenticationForm()  # Leeg formulier voor GET-verzoek
    return render(request, 'LoginSysteem/login.html', {'form': form})

# Logt de gebruiker uit
def logout_view(request):
    logout(request)  # Logt de gebruiker uit
    return redirect('login')  # Stuur door naar de loginpagina
