from django.urls import path
from . import views
urlpatterns = [
    path('products',views.products),
    path('products/<int:id>',views.product_detail),
    path('products/category/<int:id>',views.category_products),
    path('dashboard/categories',views.dashboard_categories),
    path('dashboard/categories/<int:id>',views.category_detail),
    path('dashboard/products',views.dashboard_products),
    path('dashboard/products/<int:id>',views.dashboard_product_detail),
   ]
