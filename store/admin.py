from django.contrib import admin
from store.models import ( Category, Product, ProductImages, VariationValue, Banner,Mylogo, MyFavicon)
# Register your models here.

class productImageAdmin(admin.StackedInline):
    model = ProductImages
#for slug
class ProductAdmin(admin.ModelAdmin):
    inlines = [productImageAdmin]
    prepopulated_fields = {'slug': ('name',)}
     
admin.site.register(Category)
admin.site.register(Product,ProductAdmin)
admin.site.register(VariationValue)
admin.site.register(Banner)
admin.site.register(Mylogo)
admin.site.register(MyFavicon)
 