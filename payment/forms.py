from django import forms
from payment.models import BillingAddress
#for payment mathod
from order.models import Order

class BillingAddressForm(forms.ModelForm):
    class Meta:
        model = BillingAddress
        fields = ['first_name','last_name','country','address1','address2','city','zipcode','phone_number']
        # fields =  ('__all__')
        # exclude = ('user',) 
       
        
#for payment method      
class PaymentMethodForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['payment_method']
    