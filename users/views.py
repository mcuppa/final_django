from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from users.forms import CustomPasswordChangeForm
from django.contrib.auth import update_session_auth_hash


# Create your views here.
def login_view(request):
    if request.method == 'GET':
        return render(request, 'login.html', { 'form': AuthenticationForm})
    else:
        name = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=name, password=password)
        if user is None:
            return render(request, 'login.html', { 'form': AuthenticationForm, 'error': 'Usuario y/o password incorrecto'})
        else:
            login(request,user)
            return redirect('../home/')
            

def signup(request):
    if request.method =='GET':
        return render(request, 'signup.html', { 'form' : UserCreationForm })
    else:
        if request.POST['password1']!= request.POST['password2']:
            return render(request, 'signup.html', { 'form' : UserCreationForm, 'mensaje' : 'Las contraseñas no coinciden' })
        else:
            name = request.POST['username']
            password = request.POST['password1']
            user = User.objects.create_user(username=name, password= password)
            user.save()
            return render(request, 'signup.html', { 'form' : UserCreationForm, 'mensaje' : 'Usuario registrado' })
        
@login_required
def home(request):
    return render(request, 'home.html')

def salir(request):
    logout(request)
    return redirect('../login/')



@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = CustomPasswordChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Actualiza la sesión para evitar cerrar sesión del usuario
            messages.success(request, 'Tu contraseña ha sido cambiada.')
            return redirect('profile_edit')
    else:
        form = CustomPasswordChangeForm(instance=request.user)
    return render(request, 'profile_edit.html', {'form': form})
