from decimal import Decimal
from django.conf import settings
from pages.models import Products


class Cart(object):
    def __init__(self, request):
        self.session = request.session
        
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, quantity=1, update_quantity=False, color='', size=''):
        product_id = str(product.id)
        cartkey=product_id+'*'+color+'*'+size
        #if (product_id not in self.cart) or (not(self.cart[product_id]['color']==color) and (self.cart[product_id]['size']==size)):
        if cartkey not in self.cart:
            self.cart[cartkey] = {'product_id':product_id,'prodname': product.p_name,'quantity': 0, 'price': str(product.price),'color':color, 'size':size}
        if update_quantity:
            self.cart[cartkey]['quantity'] = quantity  
        else:
            self.cart[cartkey]['product_id'] = product_id
            self.cart[cartkey]['quantity'] += quantity
            self.cart[cartkey]['color']=color
            self.cart[cartkey]['size']=size
        self.save()


    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def remove(self, cartno):
        #self.cart[cartkey]= cartno
        #product_id = str(product_id)
        #if product_id == self.cart:
        del self.cart[cartno]
        self.save()

    def __iter888__(self):
        product_ids = self.cart.keys()
        for x in product_ids:
            cartkey=x
            y = x.split("*")
            if y!= "":
               v=y[0]
               products = Products.objects.filter(id__in=v)
               for product in products:
                   self.cart[cartkey]['product'] = product

                   for item in self.cart.values():
                       item['price'] = Decimal(item['price'])
                       item['total_price'] = item['price'] * item['quantity']
                       yield item
    def __iter__(self):
        

                   for item in self.cart.values():
                       item['price'] = Decimal(item['price'])
                       item['total_price'] = item['price'] * item['quantity']
                       yield item
    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())
    def get_total_price2(self):
        return sum(Decimal(item['price']) * item['quantity']*100 for item in self.cart.values())

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True