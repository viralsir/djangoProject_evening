from django.shortcuts import render
from .models import flight
# Create your views here.
def home(request):
    return render(request,"flights/home.html",{
        "flights_info":flight.objects.all()
    })