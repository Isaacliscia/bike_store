from django.db import models

class Customer(models.Model):
	first_name = models.CharField(max_length=264)
	last_name = models.CharField(max_length=264)
	email = models.EmailField(max_length=264, unique=True)
	phone_number = models.CharField(max_length=12, unique=True)
	adress = models.CharField(max_length=264)
	city = models.CharField(max_length=264)
	country = models.CharField(max_length=264)


	def __repr__(self):
		return"<mail : {}>".format(self.email)

	def __str__(self):
		return self.email


class VehiculeType(models.Model):
	name = models.CharField(max_length=264)

	def __repr__(self):
		return"<Name: {}>".format(self.name)

	def __str__(self):
		return self.name

class VehiculeSize(models.Model):
	name = models.CharField(max_length=264)

	def __repr__(self):
		return"<Name: {}>".format(self.name)

	def __str__(self):
		return self.name

class Vehicule(models.Model):
	vehicule_type = models.ForeignKey(VehiculeType, on_delete=models.CASCADE)
	date_created = models.DateField()
	real_cost = models.CharField(max_length=140)
	size = models.ForeignKey(VehiculeSize, on_delete=models.CASCADE)

	def __repr__(self):
		return"<Vehicule : {}>".format(self.real_cost)

	def __str__(self):
		return self.real_cost


class Rental(models.Model):
	rental_date = models.DateField()
	return_date = models.DateField(null=True, blank=True)
	customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
	vehicule = models.ForeignKey(Vehicule, on_delete=models.CASCADE)

	def __repr__(self):
		return"<Rent at : {}>".format(self.rental_date)

	def __str__(self):
		return self.rental_date


class RentalRate(models.Model):
	dailyrate = models.CharField(max_length=140)
	vehicule_type = models.ForeignKey(VehiculeType, on_delete=models.CASCADE)
	vehicule_size = models.ForeignKey(VehiculeSize, on_delete=models.CASCADE)

	def __repr__(self):
		return"<Rate : {}>".format(self.dailyrate)

	def __str__(self):
		return self.dailyrate


















