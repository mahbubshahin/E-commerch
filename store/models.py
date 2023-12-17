from django.db import models
#slug
from django.template.defaultfilters import slugify
#কারেন্ট প্রোডাক্টটিকে detail.html e শো করতে 
from django.urls import reverse
# for user
from django.contrib.auth.models import User 

# Create your models here.

class Category(models.Model):
    name =models.CharField(max_length=50, blank=False, null=False)
    image = models.ImageField(upload_to='category', blank=True, null=True)
    parent =models.ForeignKey('self', related_name='children', on_delete=models.CASCADE, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-created']
        verbose_name_plural ='Categories'
    

class Product(models.Model):
    name =models.CharField(max_length=250, blank=False, null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    preview_desc =models.CharField(max_length=250, verbose_name='short Description')
    description =models.TextField(max_length=1000, verbose_name='Description')
    image = models.ImageField(upload_to='product', blank=False, null=False)
    price = models.FloatField()
    old_price= models.FloatField(default=0, blank=True, null=True)
    is_stock = models.BooleanField(default=True)
    slug = models.SlugField()
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-created']
    
    def get_product_url(self):
        return reverse('store:product_details', kwargs={'slug': self.slug})
        
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

class ProductImages(models.Model):
    Product = models.ForeignKey(Product,on_delete=models.CASCADE)
    image = models.FileField(upload_to='product_gallery')
    created = models.DateTimeField(auto_now_add=True)
        
    def __str__(self):
        return str(self.Product.name) 
    


# manager for product variation manager

class variationManager(models.Manager):
    def sizes(self):
        return super(variationManager, self).filter(variation='size')
    
    def colors(self):
        return super(variationManager, self).filter(variation='color')

#for product variation. it means product size and color

VARIATIONS_TYPE = (
    ('size', 'size'),
    ('color', 'color'),
)

class VariationValue(models.Model):
    variation = models.CharField(max_length=100, choices=VARIATIONS_TYPE)
    name = models.CharField(max_length=50)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    
    objects = variationManager()
    
    def __str__(self):
        return self.name
    
#for show daynamic data in index page
class Banner(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='banner')
    image = models.ImageField(upload_to='banner')
    is_active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
      
    def __str__(self):
        return self.product.name
    
#for logo
# User =  get_user_model()
class Mylogo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='logo')
    is_active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.image)
    
#for favicon
class MyFavicon(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='logo')
    is_active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.image)

    
    