from django.urls import path
from .views import *
urlpatterns = [
    path('', index, name="index"),
    path('add/', add_note, name="add_note"),
    path('delete/<int:pk>', delete_note, name="delete_note"),
    path('update/<int:pk>', update_note, name="update_note"),
    path('detail/<int:pk>', note_detail, name="note_detail"),
    path('register/', register_user, name="register_user"),
    path('login/', login_user, name="login_user"),
    path('logout/', logout_user, name="logout_user"),
]