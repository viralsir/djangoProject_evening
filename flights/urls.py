from django.urls import path
from .views import home,flight_info
urlpatterns=[
    path("home",home,name="flight-home"),
    path("details/<int:flight_id>",flight_info,name='flight-details')
]