from django.urls import path
from .views import *
urlpatterns = [
    path('',home,name='home'),
    path('signup/',SignUp,name='signup'),
]