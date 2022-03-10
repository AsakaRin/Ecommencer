from django.contrib import admin

# Register your models here.
from .models import Address, Author, Publisher, TradeMark, OS, Book, Electronics, Shoes, MobilePhone, Laptop, Clothes

admin.site.register(Address)
admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(TradeMark)
admin.site.register(OS)
admin.site.register(Book)
admin.site.register(Electronics)
admin.site.register(Shoes)
admin.site.register(MobilePhone)
admin.site.register(Laptop)
admin.site.register(Clothes)