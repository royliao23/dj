from django import forms


PRODUCT_QUANTITY_CHOICES = [(str(i), str(i)) for i in range(1, 26)]

pcolor='black, red'

#PRODUCT_COLORS = (( 'white', 'white'), ('blue', 'blue'), ('red', 'red'))
SIZE_CHOICES = (( 'S', 'S'), ('M', 'M'), ('L', 'L'))  
INTEGER_CHOICES= [tuple([x,x]) for x in range(1,32)]
class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    #size = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_SIZES)
    #color = forms.CharField(choices=PRODUCT_COLORS)
    #pcolor='black, red'
    
    size= forms.CharField(label="Please choose a size:", widget=forms.Select(choices=SIZE_CHOICES))
    #color= forms.CharField(label="Please choose a color:", widget=forms.Select(choices=PRODUCT_COLORS))
    #color= forms.CharField(label="Please choose a color:", widget=forms.Select(choices=getcolor(pcolor)))
    update = forms.BooleanField(label="", required=False, initial=False, widget=forms.HiddenInput)
class CartShowProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    #size = forms.CharField()
    #color = forms.CharField()
    update = forms.BooleanField(label="", required=False, initial=False, widget=forms.HiddenInput)