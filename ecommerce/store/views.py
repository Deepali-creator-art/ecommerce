from django.shortcuts import render,redirect,get_object_or_404
from .forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from .models import Product,Category

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
def LogOut(request):
    logout(request)
    return redirect('signin')
    
        
