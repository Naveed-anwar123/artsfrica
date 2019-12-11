from django.shortcuts import render
from . models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import get_user_model
from django.contrib.auth import update_session_auth_hash

# Create your views here.

def update_profile(request):
    if request.method == 'POST':
        
        if 'avatar' in request.FILES:
            image = request.FILES['avatar']
        else:
            image = ''
        about = request.POST['about']
        ex = request.POST['ex']
        education = request.POST['education']
        address = request.POST['address']
        country = request.POST['country']
        city = request.POST['city']
        zip_or_postal_code = request.POST['zip']
        phone = request.POST['phone']
        

        # Solution
        request.user.userprofile.about = address
        request.user.userprofile.ex = ex
        request.user.userprofile.education = education
        request.user.userprofile.address = address
        request.user.userprofile.country = country
        request.user.userprofile.city = city
        request.user.userprofile.zip_or_postal_code = zip_or_postal_code
        request.user.userprofile.phone = phone
        if image is not None:
            request.user.userprofile.image = image
        request.user.userprofile.save()

    
    return render(request, 'profile/update_profile.html')

@login_required
def update_account_informatin(request):
    if request.method == 'POST':
        
        if not request.POST['password'] == request.POST['cpassword']:
            return render(request, 'profile/update_account.html', {'errors':'Password does not match'})        


        request.user.first_name = request.POST['fname']
        request.user.last_name = request.POST['lname']
        if request.POST['password']:
            request.user.set_password(request.POST['password'])
            update_session_auth_hash(request, request.user)
        request.user.save()
        return render(request, 'profile/update_account.html', {'success':'Account Updated successfully!'})        

    return render(request, 'profile/update_account.html')