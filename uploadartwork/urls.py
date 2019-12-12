from django.urls import path
from . views import (
    add_artwork,
    view_artwork,
    detail_view
)

urlpatterns = [
    
    path('addnew', add_artwork, name='add_artwork' ),
    path('show', view_artwork, name='view_artwork' ),
    path('detail_view/<int:id>', detail_view, name='detail_view' ),

]