from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('products',views.products,name='products'),
    path('products/category/<int:id>',views.category_products,name='category_products'),
    path('product/<int:id>',views.product_detail,name='product_detail'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('dashboard/categories',views.categories,name='categories'),
    path('dashboard/categories/<int:id>',views.delete_category,name='delete_category'),
    path('dashboard/categories/create_category',views.create_category,name='create_category'),
    path('dashboard/update_category/<int:id>',views.update_category,name='update_category'),
    path('dashboard/products',views.dashboard_products,name='dashboard_products'),
    path('dashboard/products/<int:id>',views.delete_product,name='delete_product'),
    path('dashboard/products/create_product',views.create_product,name='create_product'),
    path('dashboard/update_product/<int:id>',views.update_product,name='update_product'),
    path('dashboard/products/search_product',views.search_product,name='search_product'),
]
