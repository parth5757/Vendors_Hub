from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.my_view, name="home"),
    path('home/', views.my_view, name="home"),
    # path('login', views.login, name="login"),
    # path('register', views.register, name="register"),
    path('user', views.User, name="user"),
    path('product', views.product, name="product"),
    path('category', views.category, name='category'),
    path('add_product', views.add_product, name="add_product"),
    path('delete_product/<int:id>/', views.delete_product, name='delete_product'),
    path('update_product/<int:id>/', views.update_product, name='update_product'),
    path('add_category', views.add_category, name="add_category"),
    path('delete_category/<int:id>/', views.delete_category, name='delete_category'),
    path('update_category/<int:id>/', views.update_category, name='update_category'),
    path('about', views.about, name='about'),
    path('<str:undefined_route>/', views.error, name='error')
]
