from dataclasses import field, fields
from .models import Product,Category
from django.forms import ModelForm
class productForm(ModelForm):
    class Meta:
        model=Product
        fields='__all__'
class categoryForm(ModelForm):
    class Meta:
        model=Category
        fields='__all__'