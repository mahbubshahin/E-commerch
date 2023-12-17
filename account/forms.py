from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from account.models import profile

#for profile form
class ProfileForm(ModelForm):
    class Meta:
        model = profile
        fields = ('__all__')
        exclude = ('user',)
