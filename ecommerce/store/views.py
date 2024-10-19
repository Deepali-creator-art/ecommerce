from django.shortcuts import render
from .forms import SignUpForm
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