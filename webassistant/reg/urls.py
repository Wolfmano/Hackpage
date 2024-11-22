from django.urls import path
from .views import *

urlpatterns = [
    path('', register, name="reg"),
    path('entry/', login_view, name="login"),
    path('logout/',logout_view, name="logout")
]