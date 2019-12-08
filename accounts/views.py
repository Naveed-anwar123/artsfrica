from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

def signin_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(username=email , password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('dashboard')
            #return render(request, 'accounts/login.html',{'error':'Success'})        
        else:
            return render(request, 'accounts/login.html',{'error':'Username or password is incorrect.!'})        
    return render(request, 'accounts/login.html')

def signup_view(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        user = User()
        user.first_name = name
        user.email = email
        user.set_password(password)
        user.is_staff = True
        user.is_superuser = False
        user.username = email.split('@')[0]
        
        try:
            user.save()
            return render(request, 'accounts/signin.html')            
        except Exception as identifier:
            return render(request, 'accounts/signup.html')        
    return render(request, 'accounts/signup.html')

def dashboard(request):
    return render(request, 'base.html')