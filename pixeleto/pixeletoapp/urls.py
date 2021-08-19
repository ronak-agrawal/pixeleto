from django.urls import path
from . import views

urlpatterns = [
    path('getuser/<int:id>', views.get_user),
    path('getallusers', views.get_all_users),
    path('adduser', views.add_user),
    path('edituser/<int:id>', views.edit_user),
    path('deleteuser/<int:id>', views.delete_user)
]
