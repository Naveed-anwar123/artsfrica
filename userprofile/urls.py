from django.urls import path
from . views import (
    update_profile,
    update_account_informatin
)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('/update-profile', update_profile, name='update_profile' ),
    path('/update-account-information', update_account_informatin, name='update_account_information' ),
]