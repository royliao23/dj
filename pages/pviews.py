from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Musician
from django.http import Http404
from django.template import loader
from django.views import generic
from .models import	Musician
from .models import Products
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render
from .forms import BlogCommentsForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import MusicianForm
from django.http import HttpResponseRedirect
#Create your views here.
#def home(request):
#return render(request,"home.html",{})

#def about(request)
#return render(request,"about.html",{})
from django.http import HttpResponse

class IndexView(generic.ListView):
    template_name="indexproducts.html"
    context_object_name='all_products'
    def get_queryset(self):
        return Products.objects.all()
class DetailView(generic.DetailView):
    models = Products
    template_name="details.html"
    queryset = Products.objects.all()

  
class MusicianCreate(CreateView):
    """docstring for Create"""
    model=Musician
    fields=['first_name','last_name','instrument','isf']
def test1(request):
   #return HttpResponse("Hello world")
   from pages.mybrother import namer
   return render(request,"test1.html",{"my_bro":namer})
   
def home(request):
   #return HttpResponse("Hello world")
   from pages.mybrother import namer
   return render(request,"home.html",{"my_bro":namer})
def about(request):

   #return HttpResponse("About world") 
   return render(request,"about.html",{}) 
def contact(request):
   #return HttpResponse("About world") 
   return render(request,"contact.html",{}) 
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


    

    
    

