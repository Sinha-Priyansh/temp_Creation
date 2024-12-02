from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def veg(request):
    return HttpResponse("<h1>If You Eat Vegie You will Die Soon</h1>")

def non_veg(request):
    return render(request,'nonveg.html')