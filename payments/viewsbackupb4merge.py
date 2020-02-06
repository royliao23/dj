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
	
    if request.method == 'POST':

        charge = stripe.Charge.create(
            amount=500,
            currency='usd',
            description='A Django charge',
            source=request.POST['stripeToken']
            
        )
        status='Your payment is processed successfully!'
        context={'status':status,}
        
        return render(request, 'homep.html',context)
        
        
        #return render(request, 'homep.html')

def callback(request):
 
  #profile = UserProfile.objects.get(user=request.user)

  r = request.post('https://connect.stripe.com/oauth/token', params={
    'client_secret': settings.STRIPE_SECRET_KEY,
  
    'grant_type': 'authorization_code'
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