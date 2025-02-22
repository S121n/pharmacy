from django.contrib import messages
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.shortcuts import redirect, render

CustomUser = get_user_model()

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        national_code = request.POST['national_code']

        #Checking
        if password != confirm_password:
            messages.error(request, 'Passwords do not match')
            return redirect('signup')

        if CustomUser.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken')
            return redirect('signup')
        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, 'Email already taken')
            return redirect('signup')

        #save
        user = CustomUser.objects.create(
            username=username,
            email=email,
            password=make_password(password),
            national_code=national_code
        )
        return redirect('home')

    return render(request,'home.html')
# LOGIN
def log_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')

    return render(request,'home.html')
# LOGOUT
def sign_out(request):
    logout(request)
    messages.success(request, 'You are now logged out')
    return redirect('home')


