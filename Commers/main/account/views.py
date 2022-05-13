import django
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout
from account.forms import loginForm, userForm,dashboardForm
from .models import CustomUser
from django.contrib.auth.decorators import login_required
# Create your views here.
def user_login(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method=='POST':
        form=loginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=authenticate(request,username=username,password=password)
            if user is not None:
                if user.is_active:
                    login(request,user)
                return redirect('home')
    else:   
        form=loginForm()
    return render(request,'login.html',{'form':form})

def user_logout(request):
    logout(request)
    return redirect('home')
def user_register(request):
    form=userForm()
    if request.method=='POST':
        form=userForm(request.POST)
        if form.is_valid:
            user=form.save(commit=False)
            user.save()
            login(request,user)
            return redirect('home')
    return render(request,'register.html',{'form':form})
def users(request):
    users=CustomUser.objects.all()
    return render(request,'users.html',{'users':users})
def delete_user(request,id):
    user=CustomUser.objects.get(id=id)
    user.delete()
    return redirect('users')
def update_user(request,id):
    user=CustomUser.objects.get(id=id)
    form=dashboardForm(instance=user)
    if request.method=='POST':
        form=dashboardForm(request.POST,instance=user)
        if form.is_valid:
            form.save()
            return redirect('home')
    return render(request,'update_user.html',{'form':form})
def create_user(request):
    form=dashboardForm()
    if request.method=='POST':
        form=dashboardForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('users')
    return render(request,'create_user.html',{'form':form})
