from django.shortcuts import render, get_object_or_404
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from pages.models import Products,Sku
from .models import Post, Like
from django.http import HttpResponse


def order_create(request):
    #cart=scart
    
    cart = Cart(request)

    print(cart.cart)
    #request.session['cart']=cart
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                product_id=item['product_id']
                quantity=item['quantity']
                product = get_object_or_404(Products, id=product_id)
                #cart.cart['product']=product
                OrderItem.objects.create(
                    order=order,
                    product=product,
                    price=item['price'],
                    size=item['size'],
                    colour=item['color'],
                    quantity=item['quantity'],

                    

                )
                skuproduct = Sku.objects.filter(product= product,colour=item['color'],size=item['size'])
                print(skuproduct[0].stock)
                id=skuproduct[0].id
                print(id)
                newq=Sku.objects.get(id=id)
                newstock=int(skuproduct[0].stock)-quantity
                newq.stock=newstock
                newq.save()
                print('after:'+str(newstock))

            cart.clear()
        return render(request, 'orders/order/created.html', {'order': order, 'cart':cart})
    else:
        form = OrderCreateForm()
    return render(request, 'orders/order/create.html', {'form': form, 'cart':cart},)

def order_create2(request,cart):
    #cart=scart
    request.session['foo']='bar'
    x=request.session.get('foo')

    cart = Cart(request)
    #request.session['cart']=cart
    form = OrderCreateForm()
    if request.method == 'POST':
        print('PPPPPPPPPPPPPPPPPPPPPPP')
        form = OrderCreateForm(request.POST)
        pass
            #cart.clear()
        return render(request, 'orders/order/created.html', {'order': order})
    else:
        
        print(cart)
        print('nnnnnnnnnnnnnnnnnnnnnnnnnnnn')
        return render(request, 'orders/order/create.html', { 'form': form,'cart':cart,'x':x})
def postlist(request):
        posts = Post.objects.all()  # Getting all the posts from database
        return render(request, 'orders/order/postlist.html', { 'posts': posts })    

def likePost(request):
        print('roy')
        if request.method == 'GET':
               post_id = request.GET['post_id']

               likedpost = Post.obejcts.get(pk=post_id) #getting the liked posts
               m = Like(post=likedpost) # Creating Like Object
               m.save()  # saving it to store in database
               return HttpResponse("Success!") # Sending an success response
        else:
               return HttpResponse("Request method is not a GET")