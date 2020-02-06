from django import forms
from .models import BlogComments
from .models import Musician, Customer, Order
from .models import Ffile

class BlogCommentsForm(forms.ModelForm):
    class Meta:
        model= BlogComments
        fields= ["firstname", "lastname", "email", "comment"]

class MusicianForm(forms.ModelForm):
    class Meta:
        model= Musician
        exclude = []
class FfileForm(forms.ModelForm):
    class Meta:
        model= Ffile
        fields= ["name", "filepath"]


INTEGER_CHOICES= [tuple([x,x]) for x in range(1,32)]

class UserForm(forms.Form):
    first_name= forms.CharField(max_length=100)
    last_name= forms.CharField(max_length=100)
    email= forms.EmailField()
    age= forms.IntegerField()
    choose_size= forms.IntegerField(label="Please choose a size:", widget=forms.Select(choices=INTEGER_CHOICES))
class CustomerForm(forms.ModelForm):
    class Meta:
        model= Customer
        exclude = ['membership','discount']
class OrderForm(forms.ModelForm):
    class Meta:
        model= Order
        exclude = ['customerid','date','active']    
from django import forms


class ContactForm(forms.Form):
    name= forms.CharField(max_length=500, label="Name")
    email= forms.EmailField(max_length=500, label="Email")
    comment= forms.CharField(label='',widget=forms.Textarea(
                        attrs={'placeholder': 'Enter your comment here'}))
        