from django.shortcuts import render
from . models import UserProfile
from django.contrib.auth.models import User
# Create your views here.

def update_profile(request):
    if request.method == 'POST':
        
        if 'avatar' in request.FILES:
            image = request.FILES['avatar']
        
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
        if image:
            request.user.userprofile.image = image
        request.user.userprofile.save()


    return render(request, 'profile/update_profile.html')


def update_account_informatin(request):
    return render(request, 'profile/update_account.html')