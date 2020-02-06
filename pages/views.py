from django.shortcuts import render, get_list_or_404, get_object_or_404,redirect
from .models import Musician
from django.http import Http404
from django.template import loader
from django.views import generic
from .models import	Musician
from .models import Category, Products, Customer, Order, Orderdetail,Post,Sku
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render
from .forms import BlogCommentsForm, UserForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import MusicianForm, CustomerForm, OrderForm,ContactForm
from django.http import HttpResponseRedirect
from cart.forms import CartAddProductForm
from cart.cart import Cart
from django.core.mail import EmailMessage
from django.core.mail import send_mail
#Create your views here.
#def home(request):
#return render(request,"home.html",{})

#def about(request)
#return render(request,"about.html",{})
from django.http import HttpResponse

class IndexView(generic.ListView):
    
    template_name="indexproduct.html"
    context_object_name='all_products'
    def get_queryset(self):
        return Products.objects.all()
class DetailView(generic.DetailView):
    models = Products
    template_name="productdetails.html"
    queryset = Products.objects.all()

  
class MusicianCreate(CreateView):
    """docstring for Create"""
    model=Musician
    fields=['first_name','last_name','instrument','isf']

  
def home(request):
   #return HttpResponse("Hello world")
   from pages.mybrother import namer
   return render(request,"home.html",{"my_bro":namer})
def about(request):

    
   #return HttpResponse("About world") 
   return render(request,"g/index.html")
def contact(request):
   #return HttpResponse("About world") 
   #return redirect('pages:contact')
   return render(request,"contact.html",{})
   #return render(request, contact(request), {})
def mid(request, key):
    from .redirect import redirect_view
    try:
        musician = Musician.objects.get(pk=key)
    except Musician.DoesNotExist:
        raise Http404("musician not exist!")
    return render(request, 'details.html', {'musician': musician,'redirect':redirect_view(request, "Hello,Viewers!")})
    #return render(request, 'test1.html', {'musician': musician,'redirect':redirect_view(request, "Hello,Viewers!")})
  # return render(request,"contact.html",{}) 
def index(request):
    all_musicians = Musician.objects.all()
    template=loader.get_template('index.html')
    context = {
           'all_musicians':all_musicians,
    }

    return HttpResponse(template.render(context,request))
   #return HttpResponse("About world") 
   #return render(request,"about.html",{}) 

def pindex(request):
    all_products = Products.objects.all()
    template=loader.get_template('indexproduct.html')
    context = {
           'all_products':all_products,
    }
def pdetail(request, key):
    from .redirect import redirect_view
    try:
        product = Products.objects.get(pk=key)
    except Products.DoesNotExist:
        raise Http404("musician not exist!")
    ##return render(request, 'productdetails.html', {'product': product,'redirect':redirect_view(request, "Hello,Viewers!")})
    #return render(request, 'test1.html', {'musician': musician,'redirect':redirect_view(request, "Hello,Viewers!")})
  # return render(request,"contact.html",{}) 
    return HttpResponse(template.render(context,request))
def indexstar(request):
    from .redirect import redirect_view
    all_musicians = Musician.objects.all()
    try:
        selected_m=all_musicians.get(pk=request.POST['musician'])
    except (KeyError,Musician.DoesNotExist):
        return render(request, 'indexstar.html', {'errormsg':"musician not selected",})
    selected_m.isf = True
    selected_m.save()
    return render(request, 'indexstar.html', {'musician': all_musicians,})


def indexs(request):
    all_musicians = Musician.objects.all()
    template=loader.get_template('indexstar.html')
    context = {
           'all_musicians':all_musicians,
    }

    return HttpResponse(template.render(context,request))
    #return HttpResponseRedirect("/indexstar")
def showform(request):

    form= BlogCommentsForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = BlogCommentsForm()
        messages.success(request, 'Form submission successful')

    context= {'form':form }
        
    return render(request, 'Blog/blogp.html', context)



@login_required(login_url='/admin/login/?next=/admin/')
def editpost(request, id):

        obj= get_object_or_404(Musician, id=id)


        #form = MusicianForm(request.POST or None, instance= obj)
        #form = MusicianForm(request.FILES or None, request.POST or None, instance=obj)
        #form = form_class(data=request.POST, files=request.FILES, instance=thing) add /upload
        form = MusicianForm(request.POST or None, request.FILES or None, instance=obj)
     #   context={'form': form}


        if form.is_valid():
                obj= form.save(commit= False)

                obj.save()

                messages.success(request, "You successfully updated the post")

                context= {'form': form}

                return render(request, 'Blog/edit.html', context)

        else:
                context= {'form': form,
                           'error': 'The form was not updated successfully. Please enter in a title and content'}
                return render(request,'Blog/edit.html' , context)

@login_required(login_url='/admin/login/?next=/admin/')
def musician_delete_view(request, id=None):

    musician= get_object_or_404(Musician, id=id)
    #return render(request, 'Blog/musician-delete-viewv2.html', context)

    if request.method == "POST":
        musician.delete()
        #messages.success(request, "Post successfully deleted!")
        return HttpResponseRedirect("/index")

    context= {'musician': musician,  }
    return render(request, 'Blog/musician-delete-viewv2.html', context)
def confirm(request, pk):

    if request.method == 'POST':
            if request.POST.get('first_name')  and request.POST.get('last_name') and request.POST.get('address') and request.POST.get('email') and request.POST.get('mobile'):
                customer=Customer()
                customer.first_name= request.POST.get('first_name')
                #customer.customerno= 11
                customer.last_name= request.POST.get('last_name')
                customer.address= request.POST.get('address')
                customer.email= request.POST.get('email')
                customer.mobile= request.POST.get('mobile')
                customer.save()
                mess="saved!"   
                return render(request, 'createpost.html',{'ss':mess})    
        #return render(request, 'confirm.html')  
    else:
                fmess=""
                return render(request,'createpost.html',{'ss':fmess})
   

def test1(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = UserForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
          timesheet = form.save(commit=False)
          timesheet.studentID = request.POST.get('first_name')
          timesheet.studentName = request.POST.get('last_name')
          timesheet.save()
          #return HttpResponseRedirect(reverse('hrfinance/timesheet.html')
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            #return HttpResponseRedirect('/index/')
          return render(request, 'test1.html', {'form': form})   


    # if a GET (or any other method) we'll create a blank form
    else:
        form = UserForm()

    return render(request, 'test1.html', {'form': form})   

def createpost(request):
        order=Order()
        if request.method == 'POST':
            if request.POST.get('first_name')  and request.POST.get('last_name') and request.POST.get('address') and request.POST.get('email') and request.POST.get('mobile'):
                customer=Customer()
                customer.first_name= request.POST.get('first_name')
                #customer.customerno= 11
                customer.last_name= request.POST.get('last_name')
                customer.address= request.POST.get('address')
                customer.email= request.POST.get('email')
                customer.mobile= request.POST.get('mobile')
                customer.save()
                custno= customer.id
                cust=str(custno)
                
                order.customerid= custno
                #customer.customerno= 11
                order.orderdate= datetime.date.today
                order.delivery= request.POST.get('delivery')
                order.note= request.POST.get('note')
                order.paymentmethod= request.POST.get('payment')
                order.save()


                mess="saved!"+cust
                return render(request, 'createpost.html',{'ss':mess})    
        #return render(request, 'confirm.html')  
        else:
                fmess=""
                return render(request,'createpost.html',{'ss':fmess})
def customerorder(request):

        if request.method == 'POST':
          customerform=CustomerForm(request.POST)
          orderform=OrderForm(request.POST)
          if customerform.is_valid() and orderform.is_valid():
            customer=customerform.save()
            order=orderform.save(False)
            order.customer=order
            order=orderform.save()
            fmess='Your Orders are Saved!'

            customerform=CustomerForm()
            orderform=OrderForm() 
            largs={'ss':fmess}
            #args.update(request)
            largs['customerform']=customerform
            largs['orderform']=orderform 
            return render(request,'confirm.html',largs)        
    
            #return render(request,'confirm.html',{'ss':fmess})        
             
        else:
          customerform=CustomerForm()
          orderform=OrderForm()
          args={}
          args.update(request)
          args['customerform']=customerform
          args['orderform']=orderform 
          return render(request,'confirm.html',args) 

def product_list(request, category_slug=None):
    cart=Cart(request)
    print(cart)
    categories = Category.objects.all()
    products = Products.objects.filter(available='True')
    print(categories)
    context = {
        'categories': categories,
        'category': categories,
        'products': products,
        'cart':cart
    }
    return render(request, 'indexproduct.html', context)
def category_select(request, pk):
    cart=Cart(request)
    categories = Category.objects.all()
    category = get_object_or_404(Category, id=pk)
    print(category)
    sproduct=Products.objects.filter(category=category, available='True')
    context = {
        'categories': categories,
        'category': category,
        'products': sproduct,
        'cart':cart
    }
    return render(request, 'indexproduct.html', context)

def product_detail(request, pk):
    
    product = get_object_or_404(Products, id=pk, available=True)
    pcolor=product.slc
    PRODUCT_COLORS=''
    singlecolor=pcolor.split(',')
    
    cart=Cart(request)
    cart_product_form = CartAddProductForm()
    context = {
        'pcolor':singlecolor,
        'product': product,
        'cart_product_form': cart_product_form,
        'cart':cart
    }
    return render(request, 'productdetails.html', context)    
    
import json      
from django.http import HttpResponse
from django.template import Template, Context
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def ajax(request):
    if request.method == "POST": #os request.GET()
        print(request)
        pcode= request.POST['pcode'].strip()
        color= request.POST['color'].strip()
        size= request.POST['size'].strip()
        quantity= request.POST['quantity']
        #sku=pcode+'*'+color+'*'+size
        
        sproduct=Sku.objects.filter(product_code=pcode,colour=color,size=size)
        #sproduct=Sku.objects.filter(product_code='33ww',colour='baby pink',size='S')
        #sproduct=Sku.objects.filter(sku='33ww*baby pink*S')
        print(sproduct)
        if sproduct.count() == 0:
            stock=0
        else:
            stock=sproduct[0].stock 
        
        #sproduct=Sku.objects.raw('SELECT * FROM pages_sku ')
            
        
    """returns json response"""
    #newvalue='roy'
    return HttpResponse(json.dumps({'pcode': pcode,'color': color,'size': size,'quantity': quantity,'stock': stock}), content_type="application/json")

def aindex(request):
    """simple index page which uses jquery to make a single get request to /ajax, alerting the value of foo"""
    return render(request, 'try.html', {})
# Create your views here.

import json
def post(request):
    if request.method == "POST": #os request.GET()
        get_value= request.body
        # Do your logic here coz you got data in `get_value`
        data = {}
        data['result'] = 'you made a request'
        return HttpResponse(json.dumps(data), content_type="application/json")



def contactview(request):
    name=''
    email=''
    comment=''


    form= ContactForm(request.POST or None)
    if form.is_valid():
        name= form.cleaned_data.get("name")
        email= form.cleaned_data.get("email")
        comment=form.cleaned_data.get("comment")


        comment= name + " with the email, " + email + ", sent the following message:\n\n" + comment;
        send_mail('Thanks for the  order!', comment, 'yunzhi.liao@gmail.com', [email])

        msg = EmailMessage('Thanks for the  order!', comment, 'yunzhi.liao@gmail.com', [email])
        msg.content_subtype = "html"  
        msg.attach_file('static/images/p3.jpg')
        msg.send()

        form= ContactForm()
        context= {'form': form}
        
        return render(request, 'contact.html', context)

    else:
        context= {'form': form}
        return render(request, 'contact.html', context)


