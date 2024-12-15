# TROMBI/views.py
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib.auth import login
from .forms import EtudiantForm
from django.contrib.auth.forms import AuthenticationForm




def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirige vers la page de login après inscription
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Remplace 'home' par la vue où tu veux rediriger l'utilisateur après la connexion
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def modifier_etudiant(request, pk):
    etudiant = get_object_or_404(Etudiant, pk=pk)
    if request.method == 'POST':
        form = EtudiantForm(request.POST, instance=etudiant)
        if form.is_valid():
            form.save()
            return redirect('etudiant_detail', pk=etudiant.pk)  # Redirige vers une page de détail de l'étudiant
    else:
        form = EtudiantForm(instance=etudiant)
    return render(request, 'modifier_etudiant.html', {'form': form})

def profil(request):
    # Code pour gérer le profil de l'utilisateur
    return render(request, 'profil.html')