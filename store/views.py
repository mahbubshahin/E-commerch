from django.shortcuts import render
from django.views.generic import ListView, DetailView,TemplateView
# Create your views here.

#product model
from store.models import Category, Product, ProductImages, Banner


class HomeListView(TemplateView):
    template_name = 'store/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['banners'] = Banner.objects.filter(is_active=True).order_by('-id')[:5]
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        category_id = request.GET.get('category_id')  # Get the category ID from the URL parameter
        if category_id:
            # If category_id is provided, filter products by the selected category
            products = Product.objects.filter(category_id=category_id).order_by('-id')
        else:
            # Otherwise, show all products
            products = Product.objects.all().order_by('-id')
        context['products'] = products
        return render(request, self.template_name, context)
    
      #show search data
    def post(self, request, *args, **kwargs):
        if request.method == 'post' or request.method == 'POST':
            search_product = request.POST.get('search_product')
            products = Product.objects.filter(name__icontains=search_product).order_by('-id')

            context = {
                'products': products
            }
            return render(request, 'store/index.html', context)


#for multiple data show.    
class ProductDeleteView(DetailView):
    model = Product
    template_name = 'store/product.html'
    context_object_name = 'item'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product_images'] = ProductImages.objects.filter(Product=self.object.id)
        return context
# def product_details(request, pk):
#     item = Product.objects.get(id=pk)
#     photos = ProductImages.objects.filter(product=iterm).order_by('-created)
#     context = {
#         'item': item,
#          'photos': photos,
#     }
#     return render(request,'store/product.html',context)
#     এটি উপরের ক্লাসবেজভিউ  এর ফাংশনভিউ




