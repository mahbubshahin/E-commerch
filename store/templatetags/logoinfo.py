#for show logo image from store models
from django import template
from store.models import MyFavicon, Mylogo


register = template.Library()

@register.filter
def logo(request):
    if request:
       logo = Mylogo.objects.filter(is_active=True).order_by('-id').first()
       return logo.image.url
    else:
        logo = Mylogo.objects.filter(is_active=True).order_by('-id').first()
        return logo.image.url
        
 
@register.filter
def favicon(user):
    if user.is_authenticated:
       logo = MyFavicon.objects.filter(user=user, is_active=True).order_by('-id').first()
       return logo.image.url 