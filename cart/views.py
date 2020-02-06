from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from pages.models import Products
from .cart import Cart
from .forms import CartAddProductForm, CartShowProductForm
import json  


@require_POST
def cart_addsimple(request, product_id):
    
    cart = Cart(request)
    product = get_object_or_404(Products, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'], update_quantity=cd['update'])
    return redirect('cart:cart_detail')
def cart_add(request, product_id):
    
    cart = Cart(request)
    product = get_object_or_404(Products, id=product_id)
    
    color=request.POST.get('color')
    print(color)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'], update_quantity=cd['update'],color=color, size=cd['size'])
    return redirect('cart:cart_detail')
def cart_add2(request, cartno):
    y = cartno.split("*")
    if y!= "":
            product_id=int(y[0])
            color=y[1]
            size=y[2]
            cart = Cart(request)
            product = get_object_or_404(Products, id=product_id)
            form = CartShowProductForm(request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                cart.add(product=product, quantity=cd['quantity'], update_quantity=cd['update'],color=color, size=size)
                return redirect('cart:cart_detail')

def cart_remove(request,cartno):
    cart = Cart(request)
    #product = get_object_or_404(Products, id=product_id)
    cart.remove(cartno)
    return redirect('cart:cart_detail')


def cart_detail(request):
    
    cart = Cart(request)
    for item in cart:
        product = get_object_or_404(Products, id=item['product_id'])
        prodpic=product.pic
        item['update_quantity_form'] = CartShowProductForm(initial={'quantity': item['quantity'], 'update': True})
        item['prodpic']=prodpic
        item['cartno']=item['product_id']+'*'+item['color']+'*'+item['size']
        item['product']=product
    #jcart=json.stringify(cart)
    #scart=encodeURI(cart)
   
    return render(request, 'cart/detail.html', {'cart': cart, })
