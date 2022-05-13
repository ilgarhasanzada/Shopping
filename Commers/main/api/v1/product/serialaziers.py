from rest_framework.serializers import ModelSerializer
from product.models import Category,Product
class CategorySerialaizer(ModelSerializer):
    class Meta:
        model=Category
        fields="__all__"
class ProductSerialaizer(ModelSerializer):
    class Meta:
        model=Product
        fields="__all__"