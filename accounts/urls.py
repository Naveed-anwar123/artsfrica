from django.urls import path
from . views import (
    signin_view,
    signup_view,
    dashboard,
    unauthorized,
    logout_view
)

urlpatterns = [
    path('signin', signin_view, name='signin' ),
    path('signup', signup_view, name='signup' ),
    path('logout', logout_view, name='logout' ),
    path('unauthorized', unauthorized, name='unauthorized' ),   
]