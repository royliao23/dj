from django.shortcuts import render, get_object_or_404,redirect
from orders.models import OrderItem
from orders.forms import OrderCreateForm
from cart.cart import Cart

from pages.models import Products,Sku

from django.http import HttpResponse
from django.core.mail import EmailMessage
from django.core.mail import send_mail




import stripe # new

from django.conf import settings
from django.views.generic.base import TemplateView
from django.shortcuts import render # new

stripe.api_key = settings.STRIPE_SECRET_KEY # new



class HomePageView(TemplateView):
    template_name = 'homep.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['key'] = settings.STRIPE_PUBLISHABLE_KEY
        return context


def charge(request): # new
    cart = Cart(request)
    amt=cart.get_total_price2()
    print(amt)
    if request.method == 'POST':

        charge = stripe.Charge.create(
            amount=int(amt),
            currency='usd',
            description='A Django charge',
            source=request.POST['stripeToken']
            
        )



        






        status='success'
        context={'status':status,}
        
        #return render(request, 'charge.html',context)
        return redirect('payments:order_create')

def callback(request):
 
  #profile = UserProfile.objects.get(user=request.user)

  r = request.POST('https://connect.stripe.com/oauth/token', params={
    'client_secret': settings.STRIPE_SECRET_KEY
  
  }).json()

  try:
    access_token = r['access_token']
    refresh_token = r['refresh_token']
    publishable_key = r['stripe_publishable_key']
    #profile.save()

    messages.success(request, "Your account was successfully connected to Stripe.")
  except KeyError:
    messages.error(request, "Unable to connect your account to Stripe.")

  return redirect('homep')

def order_create(request):
    #cart=scart
    
    cart = Cart(request)

    
    print(cart.cart)
    #request.session['cart']=cart
    if request.method == 'POST':
        print('start to work on db')
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(False)
            for item in cart:
                print(item)
                product_id=item['product_id']
                quantity=item['quantity']                 
                product = get_object_or_404(Products, id=product_id)
                sproduct = Sku.objects.filter(product= product,colour=item['color'],size=item['size'])
                if sproduct.count() == 0:
                    stock=0
                    
                else:
                    
                    order = form.save()
                    stock=sproduct[0].stock
                    OrderItem.objects.create(
                    order=order,
                    product=product,
                    price=item['price'],
                    size=item['size'],
                    colour=item['color'],
                    quantity=item['quantity'],
                )
                    print(sproduct[0].stock)
                    id=sproduct[0].id
                    print(id)
                    newq=Sku.objects.get(id=id)
                    newstock=int(sproduct[0].stock)-quantity
                    newq.stock=newstock
                    newq.save()
                    print('after:'+str(newstock))
                
            
            
            cart.clear()
            #return redirect('payments:homep')
        return render(request, 'orders/order/created.html', {'order': order, 'cart':cart})
    else:
        form = OrderCreateForm()
        print('blank')
    return render(request, 'homep.html', {'form': form, 'cart':cart,})