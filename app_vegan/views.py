from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login

from django.shortcuts import redirect

def register(request):
    if request.method == 'POST':
        # Get form data from POST request
        nome = request.POST['nome']
        apelido = request.POST['apelido']
        username = request.POST['username']
        email = request.POST['email']
        contacto = request.POST['contacto']
        password = request.POST['password']

        # Create a new user
        user = User.objects.create(
            nome=nome,
            apelido=apelido,
            username=username,
            email=email,
            contacto=contacto,
            password=password,
        )

        # You might want to add additional logic here (e.g., login the user)

        return redirect('index')  # Redirect to a success page or another URL

    # If it's not a POST request, you can handle it as needed
    return redirect('index')  # Redirect to another page or URL

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # Redirect to the dashboard or any other page after successful login
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password')

    return render(request, 'login/login.html')


# Create your views here.

def index(request):
    return render(request,'index.html')

def registo(request):
    return render(request,'registo/registo.html')

def login(request):
    return render(request,'login/login.html')

def dashboard(request):
    return render(request,'dashboard/dashboard.html')

def menu(request):
    return render(request,'menu/menu.html')
