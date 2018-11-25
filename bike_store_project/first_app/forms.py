from django import forms
from django.core import validators
from first_app.models import Customer, Vehicule, Rental, VehiculeType, VehiculeSize, RentalRate

class NewCustomerForm(forms.ModelForm):
	class Meta:
		model = Customer 
		fields = '__all__'

class NewRentalForm(forms.ModelForm):
	class Meta:
		model = Rental 
		fields = '__all__'

class NewVehiculeForm(forms.ModelForm):
	class Meta:
		model = Vehicule 
		fields = '__all__'

#hello la fami