from django.urls import path
from store import views

app_name = 'store'
urlpatterns = [
    path('index', views.HomeListView.as_view(), name='index'),
    path('product/<slug:slug>/', views.ProductDeleteView.as_view(), name='product_details'),
]
