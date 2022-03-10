from django.db import models

# Create your models here.

# Sub models

class Address(models.Model):

	number = models.IntegerField()
	street = models.CharField(max_length=64)
	district = models.CharField(max_length=64)
	city = models.CharField(max_length=64)
	country = models.CharField(max_length=64)

class Author(models.Model):

	name = models.CharField(max_length=64)
	biography = models.CharField(max_length=64)
	description = models.CharField(max_length=64)

class Publisher(models.Model):

	name = models.CharField(max_length=64)
	address = models.ForeignKey(Address, on_delete=models.CASCADE)

class TradeMark(models.Model):

	name = models.CharField(max_length=64)
	yearFounder = models.IntegerField()
	yearFounderUnit = models.CharField(max_length=64)
	description = models.CharField(max_length=64)

class OS(models.Model):

	name = models.CharField(max_length=64)
	created = models.CharField(max_length=64)


# -------------------------------------

# Main models

class Book(models.Model):

	title = models.CharField(max_length=64)
	summary = models.CharField(max_length=64)
	pages = models.IntegerField()
	language = models.CharField(max_length=64)
	yearPublisher = models.CharField(max_length=64)
	author = models.ForeignKey(Author, on_delete=models.CASCADE)
	publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)


class Electronics(models.Model):

	insurance = models.IntegerField()
	insuranceUnit = models.CharField(max_length=64)	
	weight = models.FloatField()
	weightUnit = models.CharField(max_length=64)
	productionAdress = models.CharField(max_length=64)
	description = models.CharField(max_length=64)
	trademark = models.ForeignKey(TradeMark, on_delete=models.CASCADE)

class Shoes(models.Model):

	size = models.IntegerField()
	color = models.CharField(max_length=64)
	material = models.CharField(max_length=64)
	trademark = models.ForeignKey(TradeMark, on_delete=models.CASCADE)

class MobilePhone(models.Model):
	
	ram = models.CharField(max_length=64)
	memories = models.CharField(max_length=64)
	trademark = models.ForeignKey(TradeMark, on_delete=models.CASCADE)
	os = models.ForeignKey(OS, on_delete=models.CASCADE)

class Laptop(models.Model):

	manufacturer = models.CharField(max_length=64)
	ram = models.CharField(max_length=64)
	memories = models.CharField(max_length=64)
	trademark = models.ForeignKey(TradeMark, on_delete=models.CASCADE)
	os = models.ForeignKey(OS, on_delete=models.CASCADE)

class Clothes(models.Model):

	color = models.CharField(max_length=64)
	material = models.CharField(max_length=64)
	trademark = models.ForeignKey(TradeMark, on_delete=models.CASCADE)