from django.urls import path
from . views import (
    add_artwork,
    view_artwork
)

urlpatterns = [
    
    path('addnew', add_artwork, name='add_artwork' ),
    path('show', view_artwork, name='view_artwork' ),

]