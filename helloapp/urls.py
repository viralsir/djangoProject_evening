from django.urls import path
from .views import home,about
urlpatterns = [
    path("home/",home,name="hello-home"),
    path("about/",about,name="about")
]