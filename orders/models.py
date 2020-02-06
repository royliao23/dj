from django.db import models
from pages.models import Products
from django.db.models import Count




class Order(models.Model):
    STATE_CHOICES = (
    ('STATE', (
            ('NSW', 'NSW'),
            ('VIC', 'VIC'),
            ('SA', 'SA'),
            ('TAS', 'TAS'),
            ('ACT', 'ACT'),
            ('NT', 'NT'),
            ('WA', 'WA'),
        ),
    
    ),
    )
    
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.EmailField()
    address = models.CharField(max_length=150)
    postal_code = models.CharField(max_length=30)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100, choices=STATE_CHOICES,default='NSW')
    country = models.CharField(max_length=100,default='AUSTRALIA')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created', )

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Products, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
   
    colour = models.CharField(max_length=100, blank=True)
    size = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity

class Post(models.Model):
        post_heading = models.CharField(max_length=200)
        user = models.CharField(max_length=50)
        password = models.CharField(max_length=50)
        name=models.CharField(max_length=50)
        email=models.CharField(max_length=100)
        post_text = models.TextField()
        def __unicode__(self):      # If python2 use __str__ if python3
            return unicode(self.user)
class Like(models.Model):
        post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
        post_text2 = models.TextField()

        def __str__(self):
            return self.post_text2

        def get_like_number(self):
            like_count =len(models.Like.objects.filter(post_text2='like'))
            return like_count




# Create your models here.
