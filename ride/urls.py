from ride.views import *
from django.urls import path
app_name="Nothing"

urlpatterns=[
    path('auto/',auto,name="auto"),
]