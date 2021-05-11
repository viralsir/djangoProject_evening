from django.urls import path
from .views import home,flight_info,book
urlpatterns=[
    path("home",home,name="flight-home"),
    path("details/<int:flight_id>",flight_info,name='flight-details'),
    path("book/<int:flight_id>",book,name="flight-book")

]