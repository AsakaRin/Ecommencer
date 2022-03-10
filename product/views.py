from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth import authenticate
from django.http.response import Http404
from django.shortcuts import render
from django.urls import reverse
from .models import Address, Author, Publisher, TradeMark, OS, Book, Electronics, Shoes, MobilePhone, Laptop, Clothes

# Create your views here.


def index(request):

	context = {
		"Book": Book.objects.all(),
		"Electronics": Electronics.objects.all(),
		"Shoes": Shoes.objects.all(),
		"MobilePhone": MobilePhone.objects.all(),
		"Laptop": Laptop.objects.all(),
		"Clothes": Clothes.objects.all()
	}

	return render(request, "product/index.html", context)

def addProduct(request, type_product):

	context = {
		"type_product": type_product,
		"author": Author.objects.all(),
		"publisher": Publisher.objects.all(),
		"trademark": TradeMark.objects.all(),
		"os": OS.objects.all()
	}

	return render(request, "product/addProduct.html", context)

def addProductToDB(request, type_product):

	if request.method == 'POST':

		if type_product == 'book':

			title = request.POST["title"]
			summary = request.POST["summary"]
			pages = request.POST["pages"]
			language = request.POST["language"]
			yearPublisher = request.POST["yearPublisher"]
			authorId = request.POST["authorId"]
			publisherId = request.POST["publisherId"]

			author = Author.objects.get(id=authorId)
			publisher = Publisher.objects.get(id=publisherId)

			book = Book(title=title, summary=summary, pages=int(pages), language=language, yearPublisher=yearPublisher, author=author, publisher=publisher)
			book.save()

		if type_product == 'electronics':

			insurance = request.POST["insurance"]
			insuranceUnit = request.POST['insuranceUnit']
			weight = request.POST['weight']
			weightUnit = request.POST['weightUnit']
			productionAdress = request.POST['productionAdress']
			description = request.POST['description']

			trademarkId = request.POST['trademarkId']

			trademark = TradeMark.objects.get(id=trademarkId)

			electronics = Electronics(insurance=int(insurance), insuranceUnit=insuranceUnit, weight=float(weight), weightUnit=weightUnit, productionAdress=productionAdress, description=description, trademark=trademark)
			electronics.save()

		if type_product == 'shoes':

			size = request.POST['size']
			color = request.POST['color']
			material = request.POST['material']
			
			trademarkId = request.POST['trademarkId']

			trademark = TradeMark.objects.get(id=trademarkId)

			shoes = Shoes(size=int(size), color=color, material=material, trademark=trademark)
			shoes.save()

		if type_product == 'mobilePhone':

			ram = request.POST['ram']
			memories = request.POST['memories']

			trademarkId = request.POST['trademarkId']

			trademark = TradeMark.objects.get(id=trademarkId)

			osId = request.POST['osId']

			os = OS.objects.get(id=osId)

			mobilePhone = MobilePhone(ram=ram, memories=memories, trademark=trademark, os=os)
			mobilePhone.save()

		if type_product == 'laptop':

			manufacturer = request.POST['manufacturer']
			ram = request.POST['ram']
			memories = request.POST['memories']

			trademarkId = request.POST['trademarkId']

			trademark = TradeMark.objects.get(id=trademarkId)

			osId = request.POST['osId']

			os = OS.objects.get(id=osId)

			laptop = Laptop(manufacturer=manufacturer, ram=ram, memories=memories, trademark=trademark, os=os)
			laptop.save()

		if type_product == 'clothes':

			color = request.POST['color']
			material = request.POST['material']

			trademarkId = request.POST['trademarkId']

			trademark = TradeMark.objects.get(id=trademarkId)

			clothes = Clothes(color=color, material=material, trademark=trademark)
			clothes.save()


		return HttpResponseRedirect(reverse('index'))

	else:
		return HttpResponse("Hello, world. You're at the polls index.")

def updateProduct(request, type_product, item_id):

	data = None

	if type_product == 'book':
		data = Book.objects.get(id=item_id)
	elif type_product == 'electronics':
		data = Electronics.objects.get(id=item_id)
	elif type_product == 'shoes':
		data = Shoes.objects.get(id=item_id)
	elif type_product == 'mobilePhone':
		data = MobilePhone.objects.get(id=item_id)
	elif type_product == 'laptop':
		data = Laptop.objects.get(id=item_id)
	elif type_product == 'clothes':
		data = Clothes.objects.get(id=item_id)

	context = {
		"type_product": type_product,
		"data": data,
		"author": Author.objects.all(),
		"publisher": Publisher.objects.all(),
		"trademark": TradeMark.objects.all(),
		"os": OS.objects.all()
	}

	return render(request, "product/editProduct.html", context)

def updateProductToDB(request, type_product):

	if request.method == 'POST':

		if type_product == 'book':

			id = request.POST["id"]
			title = request.POST["title"]
			summary = request.POST["summary"]
			pages = request.POST["pages"]
			language = request.POST["language"]
			yearPublisher = request.POST["yearPublisher"]
			authorId = request.POST["authorId"]
			publisherId = request.POST["publisherId"]

			author = Author.objects.get(id=authorId)
			publisher = Publisher.objects.get(id=publisherId)

			book = Book.objects.get(id=id)
			book.title = title
			book.summary = summary
			book.pages = int(pages)
			book.language = language
			book.yearPublisher = yearPublisher
			book.author = author
			book.publisher = publisher
			book.save()

		if type_product == 'electronics':

			id = request.POST["id"]
			insurance = request.POST["insurance"]
			insuranceUnit = request.POST['insuranceUnit']
			weight = request.POST['weight']
			weightUnit = request.POST['weightUnit']
			productionAdress = request.POST['productionAdress']
			description = request.POST['description']

			trademarkId = request.POST['trademarkId']

			trademark = TradeMark.objects.get(id=trademarkId)

			electronics = Electronics.objects.get(id=id)
			electronics.insurance = int(insurance)
			electronics.insuranceUnit = insuranceUnit
			electronics.weight = float(weight)
			electronics.weightUnit = weightUnit
			electronics.productionAdress = productionAdress
			electronics.description = description
			electronics.trademark = trademark
			electronics.save()

		if type_product == 'shoes':

			id = request.POST["id"]
			size = request.POST['size']
			color = request.POST['color']
			material = request.POST['material']
			
			trademarkId = request.POST['trademarkId']

			trademark = TradeMark.objects.get(id=trademarkId)

			shoes = Shoes.objects.get(id=id)
			shoes.size = int(size)
			shoes.color = color
			shoes.material = material
			shoes.trademark = trademark
			shoes.save()

		if type_product == 'mobilePhone':

			id = request.POST['id']
			ram = request.POST['ram']
			memories = request.POST['memories']

			trademarkId = request.POST['trademarkId']

			trademark = TradeMark.objects.get(id=trademarkId)

			osId = request.POST['osId']

			os = OS.objects.get(id=osId)

			mobilePhone = MobilePhone.objects.get(id=id)
			mobilePhone.ram = ram
			mobilePhone.memories = memories
			mobilePhone.trademark = trademark
			mobilePhone.os = os
			mobilePhone.save()

		if type_product == 'laptop':

			id = request.POST['id']
			manufacturer = request.POST['manufacturer']
			ram = request.POST['ram']
			memories = request.POST['memories']

			trademarkId = request.POST['trademarkId']

			trademark = TradeMark.objects.get(id=trademarkId)

			osId = request.POST['osId']

			os = OS.objects.get(id=osId)

			laptop = Laptop.objects.get(id=id)
			laptop.manufacturer = manufacturer
			laptop.ram = ram
			laptop.memories = memories
			laptop.trademark = trademark
			laptop.os = os
			laptop.save()

		if type_product == 'clothes':

			id = request.POST['id']
			color = request.POST['color']
			material = request.POST['material']

			trademarkId = request.POST['trademarkId']

			trademark = TradeMark.objects.get(id=trademarkId)

			clothes = Clothes.objects.get(id=id)
			clothes.color = color
			clothes.material = material
			clothes.trademark = trademark
			clothes.save()


		return HttpResponseRedirect(reverse('index'))

	else:
		return HttpResponse("Hello, world. You're at the polls index.")

def deletedProduct(request):

	return HttpResponse("Hello, world. You're at the polls index.")