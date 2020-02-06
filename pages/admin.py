from django.contrib import admin

# Register your models here.
from .models import Musician, Album, BlogComments, Ffile, Products, Customer,Order,Orderdetail,Post,Category,Sku
admin.site.register(Ffile)
admin.site.register(Musician)
admin.site.register(Album)
admin.site.register(BlogComments)
admin.site.register(Products)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Orderdetail)
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Sku)
