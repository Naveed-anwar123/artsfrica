from django.urls import path
from . views import (
    signin_view,
    signup_view,
    dashboard
)

urlpatterns = [
    path('signin', signin_view, name='signin' ),
    path('signup', signup_view, name='signup' ),
    path('dashboard', dashboard, name='dashboard' ),
]