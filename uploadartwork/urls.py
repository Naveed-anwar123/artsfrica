from django.urls import path
from . views import (
    add_artwork,
    view_artwork,
    detail_view,
    edit_view,
    update_artwork,
    collection_view,
    change_status_view,
    approved_view,
    change_approved_status_view
)

urlpatterns = [
    
    path('addnew', add_artwork, name='add_artwork' ),
    path('show', view_artwork, name='view_artwork' ),
    path('pending_approval', collection_view, name='collection_view' ),
    path('approved', approved_view, name='approved_view' ),
    path('detail_view/<int:id>', detail_view, name='detail_view' ),
    path('edit_view/<int:id>', edit_view, name='edit_view' ),
    path('update_artwork/<int:id>', update_artwork, name='update_artwork' ),
    path('change_status_view', change_status_view, name='change_status_view' ),
    path('change_approved_status_view', change_approved_status_view, name='change_approved_status_view' ),

]