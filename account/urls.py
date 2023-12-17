from django.urls import path
from account.views import login, register, logout
from account import views


urlpatterns = [
   
    path('', login, name="login"),
    path('register/', register, name="register"),
    path('logout/', logout, name="logout"),
    path('profile/', views.ProfileView.as_view(), name='profile')
]
