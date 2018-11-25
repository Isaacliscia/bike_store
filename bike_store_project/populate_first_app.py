import os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bike_store_project.settings')

import django
django.setup()


from datetime import datetime

#fake populate script
import random
from faker import Faker
from first_app.models import Customer, Vehicule, Rental, RentalRate, VehiculeSize, VehiculeType

fakegen = Faker()
type_vehicule = ('Bike','Scooter','Electric Bike')
size_vehicule = ('Small', 'Medium','Large')


def add_vehicule_type():
    for vehicule in type_vehicule:
        type_vehicul = VehiculeType.objects.get_or_create(name=vehicule)[0]
        type_vehicul.save()
    return type_vehicul

def add_size_type():
    for size in size_vehicule:
        size_vehicul = VehiculeSize.objects.get_or_create(name=size)[0]
        size_vehicul.save()
    return size_vehicul




def populate_customer (N=5):
    for entry in range(N):
        #create the User for entry 

        #create fake data for the entry 
        customer_fake_first_name = fakegen.first_name()
        customer_fake_last_name = fakegen.last_name()
        customer_fake_email = fakegen.email()
        customer_fake_phone_number = fakegen.phone_number()
        customer_fake_adress= fakegen.address()
        customer_fake_city = fakegen.city()
        customer_fake_country = fakegen.country()

         
        
        customer = Customer.objects.get_or_create(first_name=customer_fake_first_name, last_name=customer_fake_last_name, email= customer_fake_email,
            phone_number = customer_fake_phone_number, adress=customer_fake_adress, city= customer_fake_city, country= customer_fake_country)[0]

    return customer



def populate_vehicule(N=5):
    for entry in range(N):

        vehicule_fake_date_created = fakegen.date()
        vehicule_fake_fake_cost = fakegen.pyint()

        vehicule = Vehicule.objects.get_or_create(vehicule_type= add_vehicule_type(),date_created= vehicule_fake_date_created,
         real_cost= vehicule_fake_fake_cost, size=add_size_type())[0]

    return vehicule
        

def populate_rental (N=5):
    for entry in range(N):

        rental_fake_rental_date = fakegen.date_time_between(start_date='-1y', end_date='-7d',tzinfo=None)
        rental_fake_return_date = fakegen.date_time_between_dates(datetime_start=rental_fake_rental_date, datetime_end=datetime.now(), tzinfo=None)
        rental_fake_customer = populate_customer()
        rental_fake_vehicule = populate_vehicule()

         
        
        rental = Rental.objects.get_or_create(rental_date=rental_fake_rental_date, return_date=rental_fake_return_date,
            customer= rental_fake_customer, vehicule= rental_fake_vehicule)[0]


            
if __name__ == '__main__':
    print('Starting to populate ...')
    populate_rental(20)
    print('Finished populating!')








