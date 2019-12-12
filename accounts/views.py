from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import logout

def signin_view(request):
    """ Sign in view """

    if request.user.is_authenticated:
        return redirect('dashboard')   
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            user = auth.authenticate(username=User.objects.get(email=email) , password=password)
        except Exception as exc:
            return render(request, 'accounts/login.html',{'error':'Invalid email or password.'})        
        if user is not None:
            auth.login(request,user)
            return redirect('dashboard')
        else:
            return render(request, 'accounts/login.html',{'error':'Username or password.'})        
                

    return render(request, 'accounts/login.html')

def signup_view(request):
    """ Allow user to register """
    if request.user.is_authenticated:
        return redirect('dashboard')   
        
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


#@permission_required('is_superuser',login_url='/accounts/unauthorized')  // For super user only
#@staff_member_required
@login_required(login_url='/accounts/signin')
def dashboard(request):
    return render(request, 'base.html')

def unauthorized(request):
    return render(request, 'accounts/unauthorized.html')


def logout_view(request):
    logout(request)
    return redirect('dashboard')