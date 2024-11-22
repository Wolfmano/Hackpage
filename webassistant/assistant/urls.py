from django.urls import path
from .views import *

urlpatterns = [
    path("",index,name="index"),
    path('create/', ticket_create, name="create-tickets"),
    # path('check/', create_ticket, name="check-tickets"),
    # path('entry/', entry, name="entry"),
    # path('logout/', logout_view, name="logout")
]