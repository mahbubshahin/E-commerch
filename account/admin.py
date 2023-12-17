from django.contrib import admin
from account.models import profile
# Register your models here


class profileAdmin(admin.ModelAdmin):
    list_display = ('user', 'full_name', 'address','city','country','zipcode','phone','date_joined')

admin.site.register(profile, profileAdmin)
