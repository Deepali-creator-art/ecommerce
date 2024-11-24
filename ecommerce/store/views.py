from django.shortcuts import render,redirect,get_object_or_404
from .forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from .models import *
from django.core.exceptions import ObjectDoesNotExist

def home(request,category_slug=None):
    category_page=None
    products=None
    if category_slug!=None:
        category_page=get_object_or_404(Category,slug=category_slug)
        products=Product.objects.filter(category=category_page,available=True)
    else:
        products=Product.objects.all().filter(available=True)
    context={
        'category':category_page,'products':products
    }
    return render(request,'home.html',context)
def productpage(request,category_slug,product_slug):
    try:
        product=Product.objects.get(category__slug=category_slug,slug=product_slug)
    except Exception as e:
        raise e
    return render(request,'productpage.html',{'product':product})

def SignUp(request):
    if request.method=='POST':
        form=SignUpForm(request.POST)   #form object creation
        if form.is_valid():
            form.save()
    else:
        form=SignUpForm()
    context={
        'form':form
    }
    return render(request,'SignUp.html',context)
def SignIn(request):
    if request.method=='POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            username=request.POST['username']
            password=request.POST['password']
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('home')
    else:
        form=AuthenticationForm()
    context={
        'form':form
    }
    return render(request,'signin.html',context)
def activate(request,uidb64,token):
    #activate  the user by settings the is_active status to True
    try:
        uid=urlsafe_base64_decode(uidb64).decode()
        user=User._default_manager.get(pk=uid)
    except(TypeError,ValueError,OverflowError,User.DoesNotExist):
        user=None
    if user is not None and default_token_generator.check_token(user,token):
        user.is_active=True
        user.save()
        messages.success(request,"Congratulations Your account is activated")
        return redirect('home')
    else:
        messages.error(request,"Invalid activation link")
        return redirect('signin')
def LogOut(request):
    logout(request)
    return redirect('signin')
def _cart_id(request):
    cart=request.session.session_key
    if not cart:
        cart=request.session.create()
    return cart    
        
def cart_detail(request,total=0,counter=0,cart_items=None):
    try:
        cart=Cart.objects.get(cart_id=_cart_id(request))
        cart_items=CartItem.objects.filter(cart=cart,active=True)
        for cart_item in cart_items:
            total+=(cart_item.product.price*cart_item.quantity)
            counter+=cart_item.quantity
    except ObjectDoesNotExist:
        pass
    context={ 
        'cart_items':cart_items,
        'counter':counter,
        'total':total,
    }
    return render(request,'cart.html',context)
def add_cart(request,product_id):
    product=Product.objects.get(id=product_id)
    try:
        cart=Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart=Cart.objects.create(cart_id=_cart_id(request))
        cart.save()
    try:
        cart_item=CartItem.objects.get(product=product,cart=cart)
        if cart_item.quantity < cart_item.product.stock:
            cart_item.quantity+=1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item=CartItem.objects.create(
            product=product,
            quantity=1,
            cart=cart
        )
        cart_item.save()
    return redirect('cart_detail')
def cart_remove(request,product_id):
    cart=Cart.objects.get(cart_id=_cart_id(request))
    product=get_object_or_404(Product,id=product_id)
    cart_item=CartItem.objects.get(product=product,cart=cart)
    if cart_item.quantity >1:
        cart_item.quantity-=1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart_detail')      
def cart_remove_product(request,product_id):
    cart=Cart.objects.get(cart_id=_cart_id(request))
    product=get_object_or_404(Product,id=product_id)
    cart_item=CartItem.objects.get(product=product,cart=cart)
    cart_item.delete()
    return redirect('cart_detail')
 def search(request):
    products=Product.objects.filter(name__contains=request.GET['title'])
    return render(request,'home.html',{'products':products})  

def orderHistory(request):
    if request.user.is_authenticated:
        email=str(request.user.email)
        order_details=Order.objects.filter(emailaddress=email)
    return render(request,'order_list.html',{'order_details':order_details})

def viewOrder(request,order_id):
    if request.user.is_authenticated:
        email=str(request.user.email)
        order=Order.objects.get(id=order_id,emailAddress=email)
        order_items=OrderItem.objects.filter(order=order)
    return render(request,'order_detail.html',{'Order':order,'order_items':order_items})
