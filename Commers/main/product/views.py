from django.shortcuts import redirect, render
from .models import Category,Product
from .forms import categoryForm, productForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    return render(request,'home.html')
def products(request):
    categories=Category.objects.all()
    products=Product.objects.all()
    return render(request,'products.html',{'categories':categories,'products':products})
def category_products(request,id):
    categori=Category.objects.get(id=id)
    products=Product.objects.filter(product_category=categori)
    categories=Category.objects.all()
    return render(request,'category_products.html',{'categories':categories,'products':products,'category':categori})
def product_detail(request,id):
    productt=Product.objects.get(id=id)
    return render(request,'product_detail.html',{'product':productt})
def dashboard(request):
    return render(request,'dashboard.html')
def categories(request):
    categories=Category.objects.all()
    return render(request,'categories.html',{"categories":categories})
def delete_category(request,id):
    categoryy=Category.objects.get(id=id)
    categoryy.delete()
    return redirect('categories')
def create_category(request):
    form=categoryForm()
    if request.method=='POST':
        form=categoryForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('categories')
    return render(request,'create_category.html',{'form':form})
def update_category(request,id):
    categoryy=Category.objects.get(id=id)
    form=categoryForm(instance=categoryy)
    if request.method=='POST':
        form=categoryForm(request.POST,instance=categoryy)
        if form.is_valid:
            form.save()
            return redirect('categories')
    return render(request,'update_category.html',{'form':form})
def dashboard_products(request):
    categories=Category.objects.all()
    products=Product.objects.all()
    return render(request,'dashboard_products.html',{"products":products,"categories":categories})
def delete_product(request,id):
    productt=Product.objects.get(id=id)
    productt.delete()
    return redirect('dashboard_products')
def create_product(request):
    form=productForm()
    if request.method=='POST':
        form=productForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('dashboard_products')
    return render(request,'create_product.html',{'form':form})
def update_product(request,id):
    productt=Product.objects.get(id=id)
    form=productForm(instance=productt)
    if request.method=='POST':
        form=productForm(request.POST,instance=productt)
        if form.is_valid:
            form.save()
            return redirect('dashboard_products')
    return render(request,'update_product.html',{'form':form})
def search_product(request):
    if request.method=='POST':
        searched=request.POST['searched']
        products=Product.objects.filter(product_description__contains=searched)
        return render(request,'search_product.html',{'products':products})
