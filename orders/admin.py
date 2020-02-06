from django.contrib import admin
from .models import Order, OrderItem
from .models import Post, Like
from django.utils.html import format_html



#admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Post)
admin.site.register(Like)


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']
   	


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
  
  list_display = ('id', 'first_name', 'last_name', 'email', 'address', 'postal_code', 'city', 'paid', 'created',
                    'updated')
  list_filter = ['paid', 'created', 'updated']
  inlines = [OrderItemInline]
  date_hierarchy = 'created'
  search_fields = ['first_name', 'last_name', 'email']
  



# Register your models here.


# Register your models here.
