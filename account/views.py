from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as authLogin, logout as authLogout
from django.contrib.auth.models import User

from django.contrib import messages

from store.views import HomeListView

#for show user orders in her account
from order.models import Cart, Order
from payment.models import BillingAddress
from payment.forms import BillingAddressForm
from account.models import profile
from account.forms import ProfileForm
from django.views.generic import TemplateView
# Create your views here.


def login(request):
    if request.user.is_authenticated:
        return redirect('store:index')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            user = authenticate(username=username, password=password)
            if user is not None:
                authLogin(request, user)
                messages.add_message(request, messages.SUCCESS, "Successfully Logged in.")
                return redirect('store:index')
            else:
                messages.add_message(request, messages.ERROR, "Credentials are not valid.")
                return redirect('login')
    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')


        if password1 != password2:
            messages.add_message(request, messages.ERROR, "Passwords didn't match")
            return redirect("register")

        user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password1)

        authLogin(request, user)
        return redirect('store:index')

    return render(request, 'register.html')


def logout(request):
    authLogout(request)
    return redirect('login')

#customer profile show in profile page
class ProfileView(TemplateView):
    def get(self,request, *args, **kwargs):
        orders = Order.objects.filter(user=request.user, ordered=True)
        #for billing address
        billingaddress = BillingAddress.objects.get(user=request.user)
        billingAddress_form = BillingAddressForm(instance=billingaddress)
        #for user profile
        profile_obj = profile.objects.get(user = request.user)
        Profile_Form = ProfileForm(instance=profile_obj)
        #show user profile details
        
        context = {
            'orders': orders,
            'billingaddress': billingAddress_form, 
            'ProfileForm': Profile_Form,
        }
        return render(request, 'profile.html',context)
    
    def post(self,request, *args, **kwargs):
        if request.method == 'post' or request.method== 'POST':
            #for save billing address
            billingaddress = BillingAddress.objects.get(user=request.user)
            billingAddress_form = BillingAddressForm(request.POST, instance=billingaddress)
            #for save user profile 
            profile_obj = profile.objects.get(user = request.user)
            Profile_Form = ProfileForm(request.POST, instance=profile_obj)
            if billingAddress_form.is_valid() or Profile_Form.is_valid():
                billingAddress_form.save()
                Profile_Form.save()
                return redirect('account:profile')