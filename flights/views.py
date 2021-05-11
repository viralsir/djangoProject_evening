from django.shortcuts import render,redirect
from .models import flight,passenger
# Create your views here.
def home(request):
    return render(request,"flights/home.html",{
        "flights_info":flight.objects.all()
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
