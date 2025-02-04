from django.urls import path
from .views import *

from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView,PasswordChangeDoneView,PasswordResetView,PasswordResetConfirmView,PasswordResetDoneView,PasswordResetCompleteView
urlpatterns = [
urlpatterns = [
    path('',home,name='home'),
    path("category/<slug:category_slug>",home,name='products_by_category'),
    path("category/<slug:category_slug>/<slug:product_slug>",productpage,name='products_detail'),
    path("cart",cart_detail,name='cart_detail'),
    path("cart/add/<int:product_id>/",add_cart,name='add_cart'),
    path("cart/minus/<int:product_id>/",cart_remove,name='minus_cart'),
    path("cart/delete/<int:product_id>/",cart_remove_product,name='delete_cart'),
    path('order_history',orderHistory,name='order_history'),
    path('order/<int:order_id>',viewOrder,name='order_detail'),
    path('signup/',SignUp,name='signup'),
    path('signin/',SignIn,name='signin'),
    path('logout/',LogOut,name='logout'),
    path('search/',search,name='search'),
    path('activate/<uidb64>/<token>/',activate,name='activate'),
    #Set up url for password change 
    path("change_password/",PasswordChangeView.as_view(template_name='password_operations/password_change_form.html',form_class = PasswordChangeForm, success_url = '/password_change_done/'),name='change_password'),
    path("password_change_done/",PasswordChangeDoneView.as_view(template_name='password_operations/password_change_done.html'),name='password_change_done'),
    #reset password url
    path("password_reset/",Email_message.as_view(template_name='password_operations/password_reset.html'),name='password_reset'),
    path("password_reset/done/",PasswordResetDoneView.as_view(template_name='password_reset_done.html'),name='password_reset_done'),
    path("password_reset_confirm/<uidb64>/<token>/",PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),name='password_reset_confirm'),
    path("password_reset_complete/",PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),name='password_reset_complete'),
    
]
