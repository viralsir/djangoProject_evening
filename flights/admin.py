from django.contrib import admin
from .models import flight,airport,passenger

# Register your models here.
admin.site.register(airport)
admin.site.register(flight)
admin.site.register(passenger)

