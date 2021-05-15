from django.urls import path
from .views import home,flight_info,book,airport_info,airport_detail
urlpatterns=[
    path("home",home,name="flight-home"),
    path("air_home/",airport_info,name="air-home"),
    path("air_details/<int:air_id>",airport_detail, name='airport-details'),
    path("details/<int:flight_id>",flight_info,name='flight-details'),
    path("book/<int:flight_id>",book,name="flight-book")

]