from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from api.v1.product.serialaziers import CategorySerialaizer, ProductSerialaizer
from product.models import Product,Category
@api_view(['GET'])
def products(request):
    if request.method=="GET":
        categories=Category.objects.all()
        category_serialaizer=CategorySerialaizer(instance=categories,many=True)
        products=Product.objects.all()
        product_serialaizer=ProductSerialaizer(instance=products,many=True)
        return Response(data={
            "products": product_serialaizer.data,
            "categories":category_serialaizer.data
        })
@api_view(['GET'])           
def product_detail(request,id):
    try:
        product=Product.objects.get(id=id)
    except:
        return Response(data={
            "errors":204,
            "messages":f"{id}.th product don't found"
        },status=status.HTTP_204_NO_CONTENT)
    serialaizers=ProductSerialaizer(instance=product)

    return Response(data=serialaizers.data)

@api_view(['GET'])
def category_products(request,id):
    try:
        category=Category.objects.get(id=id)
    except:
        return Response(data={
            "errors":204,
            "messages":f"{id}.th category don't found"
        },status=status.HTTP_204_NO_CONTENT)
    products=Product.objects.filter(product_category=category)
    categories=Category.objects.all()
    categories_serialaizer=CategorySerialaizer(instance=categories,many=True)
    product_serialaizer=ProductSerialaizer(instance=products,many=True)
    category_serialaizer=CategorySerialaizer(instance=category)
    return Response(data={
        "Category":category_serialaizer.data,
        "Categories":categories_serialaizer.data,
        "products": product_serialaizer.data
    }) 
@api_view(['GET','POST'])
def dashboard_categories(request):
    if request.method=="GET":
        categories=Category.objects.all()
        serialaizer=CategorySerialaizer(instance=categories,many=True)
        return Response(serialaizer.data)
    elif request.method=="POST":
        serialaizer=CategorySerialaizer(data=request.data)
        if serialaizer.is_valid():
            serialaizer.save()
            return Response(data=serialaizer.data,status=status.HTTP_200_OK)
@api_view(['GET','PUT','DELETE'])
def category_detail(request,id):
    try:
        category=Category.objects.get(id=id)
    except:
        return Response(data={
            "errors":204,
            "messages":f"{id}.th category don't found"
        },status=status.HTTP_204_NO_CONTENT)
    if request.method=="GET":
        serialaizer=CategorySerialaizer(instance=category)
        return Response(serialaizer.data)
    elif request.method=="PUT":
        serialaizer=CategorySerialaizer(instance=category,data=request.data)
        if serialaizer.is_valid():
            serialaizer.save()
            return Response(serialaizer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    elif request.method=="DELETE":
        category.delete()
        return Response(
            {
                'errors':204,
                'message':f'{id}.th category was deleted'
            },status=status.HTTP_204_NO_CONTENT
        )
@api_view(['GET','POST'])
def dashboard_products(request):
    if request.method=="GET":
        categories=Category.objects.all()
        category_serialaizer=CategorySerialaizer(instance=categories,many=True)
        products=Product.objects.all()
        product_serialaizer=ProductSerialaizer(instance=products,many=True)
        return Response(data={
            "products": product_serialaizer.data,
            "categories":category_serialaizer.data
        })
    elif request.method=="POST":
        serialaizer=ProductSerialaizer(data=request.data)
        if serialaizer.is_valid():
            serialaizer.save()
            return Response(serialaizer.data,status=status.HTTP_200_OK)

@api_view(['GET','PUT','DELETE'])
def dashboard_product_detail(request,id):
    try:
        product=Product.objects.get(id=id)
    except:
        return Response(data={
            "errors":204,
            "messages":f"{id}.th product don't found"
        },status=status.HTTP_204_NO_CONTENT)
    if request.method=="GET":
        serialaizer=ProductSerialaizer(instance=product)
        return Response(data=serialaizer.data)
    elif request.method=="PUT":
        serialaizer=ProductSerialaizer(instance=product,data=request.data)
        if serialaizer.is_valid():
            serialaizer.save()
            return Response(serialaizer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    elif request.method=="DELETE":
        product.delete()
        return Response(
            {
                'errors':204,
                'message':f'{id}.th product was deleted'
            },status=status.HTTP_204_NO_CONTENT
        )

