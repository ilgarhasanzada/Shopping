from django.contrib.auth.forms import UserChangeForm,UserCreationForm
from django.forms import Form
from django import forms
from .models import CustomUser
class userForm(UserCreationForm):
    class Meta:
        model=CustomUser
        fields=('email','username','first_name')
class dashboardForm(UserCreationForm):
    class Meta:
        model=CustomUser
        fields=('username','email','first_name','is_active','is_superuser','is_staff')
class loginForm(Form):
    username=forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control'
    }))
    password=forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-control'
    }))