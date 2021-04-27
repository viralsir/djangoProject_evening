from django.shortcuts import render
from datetime import datetime
# Create your views here.
def home(request):
    date=datetime.utcnow()
    return render(request,"newyear/home.html",{
        'newyear': date.month==1 and date.day==1
    })