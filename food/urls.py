from food.views import*

from django.urls import path
app_name='anything'

urlpatterns=[
    path("veg/",veg,name='veg'),
    path('non_veg/',non_veg,name='non_veg'),

]