from django.shortcuts import render, get_object_or_404
from .models import OrderItem,Post
from .forms import OrderCreateForm
from cart.cart import Cart
from payments.views import *
from pages.models import Products,Sku
from .models import Post, Like
from django.http import HttpResponse
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from django.db.models import Count

def order_create(request):
    #cart=scart
    
    cart = Cart(request)

    print(cart.cart)
    #request.session['cart']=cart
    if request.method == 'POST':
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
                
            
            last_name=str(form.cleaned_data.get("last_name"))
            #streetno=str(form.cleaned_data.get("first_name"))
            address=str(form.cleaned_data.get("address"))
            suburb=str(form.cleaned_data.get("city"))
            post_code=str(form.cleaned_data.get("postal_code"))
            state=str(form.cleaned_data.get("state"))
            country=str(form.cleaned_data.get("country"))

            name=''
            email=''
            total=0
            comment='<p>Your order will be delivered to:</p>'+'</br>'+address+'</br>'+suburb+'</br>'+state+' '+country+'<br><br><p>You Ordeded the Folllowing:</p> </br>'
            name= str(form.cleaned_data.get("first_name"))+' '+last_name
            email=str(form.cleaned_data.get("email"))
            for item in cart:

                comment=comment+'<h4>'+item['prodname'] +':</h4>Quantity: '+str(item['quantity'])+' Price:'+str(item['price'])+' Size: ' + item['size'] +' Color: ' +   item['color']  +'<br>'+' Subtotal: '+str(item['total_price'])+'<br>'
                total=total+item['total_price']#subject= name + " with the email" + email + "sent the following message:" + comment;
           
            #send_mail('Thanks for the  order!', comment, 'yunzhi.liao@gmail.com', [email])
            comment=comment+'<p><br><h4>Total: '+str(total)+'</h4></p>'
            msg = EmailMessage('Thanks '+name+', Your order is confirmed!!', comment, 'yunzhi.liao@gmail.com', [email])
            msg.content_subtype = "html"  
            #msg.attach_file('')
            msg.send()
            cart.clear()
        return render(request, 'orders/order/created.html', {'order': order, 'cart':cart})
    else:
        form = OrderCreateForm()
    return render(request, 'orders/order/homep.html', {'form': form, 'cart':cart},)

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
        posts = Post.objects.all().annotate(ml=Count("likes"))
        likeg = Like.objects.filter(post_text2='like').annotate(mll=Count("post_text2"))
        #print(likeg[3])
        context_dict={}
        for post in posts: 
            #print(post.ml)
            likeno = Like.objects.filter(post=post,post_text2='like').count()
            post.lk=likeno
            #post.objects.annotate(mylike=likeno)
            context_dict['posts'] = post
            context_dict['likes'] = likeno
            #print(context_dict)
            print(post)
        likenum=Like.objects.filter(post_text2='like').count()
        #print(context_dict) # Getting all the posts from database
        return render(request, 'orders/order/postlist.html', { 'posts': posts, 'likenum':likenum})    

def likePost(request,pk):
        print('roy')
        if request.method == 'GET':
               post_id = request.GET['post_id']

               likedpost = Post.obejcts.get(pk=post_id) #getting the liked posts
               m = Like(post=likedpost) # Creating Like Object
               m.save()  # saving it to store in database
               return HttpResponse("Success!") # Sending an success response
        else:
               return HttpResponse("Request method is not a GET")
import json      
from django.http import HttpResponse
from django.template import Template, Context
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def ajax2(request):
    print('hi')
    if request.method == "POST": #os request.GET()
        print(request)
        print('roy')
        post_id=request.POST['post_id'].strip()
        thetext=request.POST['thetext'].strip()
        thecomment=request.POST['thecomment'].strip()
        if thetext=='Like':
            thecomment='like'
        post=Post.objects.get(pk=post_id)
        print(thecomment)
        textpost = Like(post=post,post_text2=thecomment)
        textpost.save()
        likenum=Like.objects.filter(post_text2='like').count()
        print(likenum)
        


        #sproduct=Sku.objects.raw('SELECT * FROM pages_sku ')
            
        
    """returns json response"""
    #newvalue='roy'
    return HttpResponse(json.dumps({'stock': post_id,'likenum': likenum,'thecomment':thecomment}), content_type="application/json")

def ajax3(request):
    print('hi')
    if request.method == "POST": #os request.GET()
        print(request)
        print('roy')
        post_id=request.POST['post_id'].strip()
        thecomment=request.POST['thecomment'].strip()
        post=Post.objects.get(pk=post_id)
        print(thecomment)
        textpost = Like(post=post,post_text2=thecomment)
        textpost.save()

        #sproduct=Sku.objects.raw('SELECT * FROM pages_sku ')
            
        
    """returns json response"""
    #newvalue='roy'
    return HttpResponse(json.dumps({'stock': post_id,'thecomment':thecomment}), content_type="application/json")

def commentpost(request,pk):
    
    if request.method == "POST":
        print('hi comment')
        print(request)
        print(pk)
        comment=request.POST.get('mycomment')
        print(comment)
        
        #sproduct=Sku.objects.raw('SELECT * FROM pages_sku ')
            
        
    """returns json response"""
    #newvalue='roy'
    return HttpResponse(json.dumps({'stock':'comment'}), content_type="application/json")