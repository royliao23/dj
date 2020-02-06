from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from pages.models import Products
from .cart import Cart
from .forms import CartAddProductForm, CartShowProductForm


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
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'], update_quantity=cd['update'],color=cd['color'], size=cd['size'])
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
        prodname=product.p_name
        prodpic=product.pic
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 'color':item['color'], 'size':item['size'],'update': True})
        item['prodname']=prodname
        item['prodpic']=prodpic
        item['cartno']=item['product_id']+'*'+item['color']+item['size']
    return render(request, 'cart/detail.html', {'cart': cart})
