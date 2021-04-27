from django.urls import path
from .views import home,about,greetings
urlpatterns = [
    path("home/",home,name="hello-home"),
    path("about/",about,name="about"),
    path("greetings/<str:name>",greetings,name="greet")
]