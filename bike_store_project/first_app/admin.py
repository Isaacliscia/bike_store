from django.contrib import admin
from first_app.models import Customer, Vehicule, Rental, VehiculeType, VehiculeSize, RentalRate

# Register your models here.
admin.site.register(Customer)
admin.site.register(Vehicule)
admin.site.register(VehiculeSize)
admin.site.register(VehiculeType)
admin.site.register(Rental)
admin.site.register(RentalRate)