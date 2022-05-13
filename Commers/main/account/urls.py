from django.urls import path
from . import views
urlpatterns = [
    path('login',views.user_login,name='user_login'),
    path('logout',views.user_logout,name='logout'),
    path('sign_up',views.user_register,name='register'),
    path('user',views.users,name='users'),
    path('user/<int:id>',views.delete_user,name='delete_user'),
    path('user/update/<int:id>',views.update_user,name='update_user'),
    path('user/create_user',views.create_user,name='create_user'),
]
