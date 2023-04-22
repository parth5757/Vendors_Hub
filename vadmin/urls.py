from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.my_view, name="home"),
    path('home/', views.my_view, name="home"),
    path('login', views.login, name="login"),
    path('register', views.register, name="register"),
    path('user', views.User, name="user"),
    path('product', views.product, name="product"),
    path('add_product', views.add_product, name="add_product"),
    path('delete_product/<int:id>/', views.delete_product, name='delete_product'),
    path('update_product/<int:id>/', views.update_product, name='update_product'),
]
