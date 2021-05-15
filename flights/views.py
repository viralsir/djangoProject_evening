from django.shortcuts import render,redirect
from .models import flight,passenger,airport
# Create your views here.
def home(request):
    return render(request,"flights/home.html",{
        "flights_info":flight.objects.all()
    })

def airport_info(request):
    return render(request, "flights/airport_list.html", {
        "airports":airport.objects.all()

    })

def airport_detail(request,air_id):
    airportinfo = airport.objects.get(pk=air_id)
    return render(request, "flights/airport_detail.html", {
        "airport":airportinfo,
        "airport_origin":airportinfo.departure.all(),
         "airport_arrival":airportinfo.arrival.all()
    })

def flight_info(request,flight_id):
    flightinfo=flight.objects.get(pk=flight_id)
    return render(request,"flights/flight_detail.html",{
        "flight":flightinfo,
        "passengers":flightinfo.passenger.all(),
        "non_passengers":passenger.objects.exclude(flights=flightinfo).all()
    })

def book(request,flight_id):
    if request.method=='POST':
        flightinfo=flight.objects.get(id=flight_id)
        psgn=passenger.objects.get(id=int(request.POST['non_passenger']))
        psgn.flights.add(flightinfo)
        psgn.save()
        return redirect('flight-home')
