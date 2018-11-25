from django.shortcuts import render
from first_app.models import Customer, Vehicule, VehiculeType, VehiculeSize, Rental, RentalRate
from . import forms


def get_all_customers_id(customer_id):
	customers = {'customer' : Customer.objects.filter(id = customer_id)
	}
	return customers

def get_all_rental_id(rental_id):
	rentals = {'rental' : Rental.objects.filter(id = rental_id)
	}
	return rentals

def get_all_vehicule_id(rental_id):
	vehicules = {'vehicule' : Vehicule.objects.filter(id = rental_id)
	}
	return vehicules

# Create your views here.





def index(request):
	user = {'first_name':'isaac'}
	return render(request, 'index.html', user)


def rental(request):
	last_returns = {'rentals' : Rental.objects.all().order_by('-rental_date')
	}
	return render(request, 'rental.html', last_returns)


def customer(request):
	customers = {'customer' : Customer.objects.all().order_by('-first_name')
	}
	return render(request, 'customer.html', customers)

def vehicule(request):
	vehicules = {'vehicule' : Vehicule.objects.all()
	}
	return render(request, 'vehicule.html', vehicules)






def customer_info(request, customer_id):
	return render(request, 'customer_info.html',context = get_all_customers_id(customer_id))

def rental_info(request, rental_id):
	return render(request, 'rental_info.html',context = get_all_rental_id(rental_id))

def vehicule_info(request, vehicule_id):
	return render(request, 'vehicule_info.html',context = get_all_vehicule_id(vehicule_id))





def form_customer_view(request):
	form = forms.NewCustomerForm()
	if request.method == 'POST':
		form = forms.NewCustomerForm(request.POST)
		if form.is_valid():
			form.save(commit=True)
			return customer(request)
		else: 
			print('Error - form is invalid')

	return render(request, 'form_customer.html',{'form': form})

def form_rental_view(request):
	form = forms.NewRentalForm()
	if request.method == 'POST':
		form = forms.NewRentalForm(request.POST)
		if form.is_valid():
			form.save(commit=True)
			return rental(request)
		else: 
			print('Error - form is invalid')

	return render(request, 'form_rental.html',{'form': form})

def form_vehicule_view(request):
	form = forms.NewVehiculeForm()
	if request.method == 'POST':
		form = forms.NewVehiculeForm(request.POST)
		if form.is_valid():
			form.save(commit=True)
			return vehicule(request)
		else: 
			print('Error - form is invalid')

	return render(request, 'form_vehicule.html',{'form': form})

