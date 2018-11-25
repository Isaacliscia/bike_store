from django.urls import path
from . import views

urlpatterns = [
path('', views.index, name='index'),
path('rental/', views.rental, name='rental'),
path('rental/<int:email>/',views.rental_info, name='name_info'),
path('customer/', views.customer, name='customer'),
path('customer/customer_info/<int:customer_id>/', views.customer_info, name='customer_info'),
path('customer/add/', views.form_customer_view, name='form_customer_view'),
path('rental/rental_info/<int:rental_id>/', views.rental_info, name='rental_info'),
path('rental/add/', views.form_rental_view, name='form_rental_view'),
path('vehicule/', views.vehicule, name='vehicule'),
path('vehicule/vehicule_info/<int:vehicule_id>/', views.vehicule_info, name='vehicule_info'),
path('vehicule/add/', views.form_vehicule_view, name='form_vehicule_view'),


]