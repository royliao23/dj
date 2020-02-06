from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
import datetime

class Musician(models.Model):
   # User= settings.AUTH_USER_MODEL

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)
    isf =  models.BooleanField(default=False)
    pic = models.ImageField(max_length=5000)

    def get_absolute_url(self):
    	return reverse('pg:default', kwargs={"pk":self.pk})

    def __str__(self):
    	return self.first_name+' '+self.last_name

class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()
    
class Author(models.Model):
    first_name = models.CharField(max_length=200, blank=False)
    last_name = models.CharField(max_length=200, blank=False)
    date_of_birth = models.DateField(null=True, blank =True)
    date_of_death = models.DateField(null=True, blank =True)


class BlogComments(models.Model):
    firstname= models.CharField(max_length=100)
    lastname= models.CharField(max_length=100)
    email= models.EmailField()
    comment= models.CharField(max_length=10000)

class Ffile(models.Model):
    name= models.CharField(max_length=500)
    filepath= models.FileField(upload_to='files/', null=True, verbose_name="")

    def __str__(self):
        return self.name + ": " + str(self.filepath)

class Category(models.Model):
    name = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True ,db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name', )
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('pages:category_select', kwargs={"pk":self.pk})

class Products(models.Model):
   # User= settings.AUTH_USER_MODEL
    SIZE_CHOICES = (
    ('Size', (
            ('small', 's'),
            ('medium', 'm'),
            ('large', 'l'),
            ('extr large', 'xl'),
        ),
    
    ),
    )
    #SC=('XS','S','M','L','XL','XXL')
    COLOR_CHOICES = (
    
    ('color', (
            ('white', 'white'),
            ('blue', 'blue'),
            ('red', 'red'),
        )
    ),)

    

    category = models.ForeignKey(Category, blank=True, related_name='products', on_delete=models.CASCADE)
    p_code = models.CharField(max_length=10, unique=True)
    p_name = models.CharField(max_length=10)
    slug = models.SlugField(max_length=10, db_index=True, blank=True)
    description = models.TextField()
    #category = models.CharField(max_length=100, blank=True)
    colour = models.CharField(max_length=10,choices=COLOR_CHOICES)
    size = models.CharField(max_length=10, choices=SIZE_CHOICES)
    price = models.DecimalField(decimal_places=2, max_digits=4, default=0)
    #stock = models.IntegerField(default=100)
    isf =  models.BooleanField(default=False)
    pic = models.ImageField()
    sls = models.CharField(max_length=10,default=SIZE_CHOICES)
    slc = models.CharField(max_length=10)
    
    
    available = models.BooleanField(default=True)
    stock = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)

    class Meta:
        ordering = ('p_name', )
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.p_code

    def get_absolute_url(self):
        return reverse('pages:product_detail', args=[self.id, self.slug])

class Customer(models.Model):
   # User= settings.AUTH_USER_MODEL
   # customerno = models.IntegerField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    membership =  models.BooleanField(default=False)
    email = models.EmailField(max_length=100)
    mobile = models.CharField(max_length=70)
    discount=models.DecimalField(decimal_places=2, max_digits=4, default=0)
    startdate= models.DateField(("Date"), default=datetime.date.today)
  
    

class Order(models.Model):
   # User= settings.AUTH_USER_MODEL
    DELIVERY_CHOICES = (
    
    ('Delivery Options', (
            ('tnt', 'TNT'),
            ('AUSPOST', 'AUSPOST'),
           
        )
    ),
    ('OTHERS', 'My own choice'),)
   # orderno= models.IntegerField(max_length=50)
    customerid = models.ForeignKey(Customer,null=True, blank=True, on_delete=models.SET_NULL)
    date = models.DateField(("Date"), default=datetime.date.today)
    deliverymode = models.CharField(max_length=100,choices=DELIVERY_CHOICES)
    paymethod = models.CharField(max_length=100)
    active =  models.BooleanField(default=False)
    note = models.CharField(max_length=500, blank=True)
 
    

class Orderdetail(models.Model):
   # User= settings.AUTH_USER_MODEL

    orderid = models.ForeignKey(Order,null=True, blank=True, on_delete=models.SET_NULL)
    prodcode = models.ForeignKey(Products,null=True, blank=True, on_delete=models.SET_NULL)
    
   



class Post(models.Model):
    title= models.CharField(max_length=300, unique=True)
    content= models.TextField()

class Sku(models.Model):
    sku = models.CharField(max_length=50)
    product = models.category = models.ForeignKey(Products, blank=True, related_name='products', default=1 ,on_delete=models.CASCADE)
    product_code = models.CharField(max_length=50)  
    colour = models.CharField(max_length=100)
    size = models.CharField(max_length=100)
    available = models.BooleanField(default=True)
    stock = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.product_code
   

   