from django.db import models

# Create your models here.
class Category(models.Model):
    category_name=models.CharField(max_length=200)
    def __str__(self) -> str:
        return self.category_name
class Product(models.Model):
    product_category=models.ForeignKey(Category,on_delete=models.SET_NULL,blank=True,null=True)
    product_name=models.CharField(max_length=500)
    product_description=models.CharField(max_length=500)
    add_time=models.DateTimeField(auto_now_add=True,null=True)
    def __str__(self) -> str:
        return self.product_name

