from django import forms 
from django.contrib.auth.models import User #table create
from django.contrib.auth.forms import UserCreationForm #form creation
class SignUpForm(UserCreationForm):
    address=forms.CharField(max_length=50)
    class Meta:
        model=User
        fields=['username','password1','password2','first_name','last_name','email','address']
