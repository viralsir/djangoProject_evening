from django.shortcuts import render
from .models import flight
# Create your views here.
def home(request):
    return render(request,"flights/home.html",{
        "flights_info":flight.objects.all()
    })

def flight_info(request,flight_id):
    flightinfo=flight.objects.get(pk=flight_id)
    return render(request,"flights/flight_detail.html",{
        "flight":flightinfo,
        "passengers":flightinfo.passenger.all()
    })