from django import forms

#for coupone code. it define in model in this app
class CouponCodeForm(forms.Form):
    code = forms.CharField()