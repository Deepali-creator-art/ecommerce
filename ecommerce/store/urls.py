from django.urls import path
from .views import *
urlpatterns = [
    path('',home,name='home'),
    path("category/<slug:category_slug>",home,name='products_by_category'),
    path('signup/',SignUp,name='signup'),
    path('signin/',SignIn,name='signin'),
    path('logout/',LogOut,name='logout'),
]