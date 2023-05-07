from django.urls import path,include
from . import views

urlpatterns = [
    path('signin', views.signin, name="signin"),
    path('register', views.register, name="register"),
    path('signup', views.signup, name="signup"),
    path('<str:undefined_route>/', views.error, name='error'),
]
