from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
# return HttpResponse("<h1>hello</h1>");
    return render(request,"helloapp/home.html",{
        'title':"Home"
    })

def about(request):
   # return HttpResponse("<h1>About page </h1>");
    return render(request,"helloapp/about.html",{
        'title':'About'

    })

def greetings(request,name):
   # return HttpResponse(f"<h1>Hello {name} </h1>");
    return render(request,"helloapp/greetings.html",
                  {'username':name,
                   'title':'greetings'
                   })