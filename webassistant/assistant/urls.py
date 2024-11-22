from django.urls import path
from .views import *

urlpatterns = [
    path("",index,name="index"),
    # path('create/', ticket_create, name="create-tickets"),

]