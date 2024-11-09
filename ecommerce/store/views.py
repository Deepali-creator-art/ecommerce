from django.shortcuts import render,redirect
from .forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
def home(request):
    return render(request,'home.html')

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
    
        
