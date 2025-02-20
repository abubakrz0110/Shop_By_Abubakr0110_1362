
from django.contrib import admin
from django.urls import path
from apps.views import IndexView, ShopView, AboutView, ContactView, Shop_SingleView, UserCreateView, UserLoginView, UserLogOutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", IndexView.as_view(), name="index"),
    path("shop/", ShopView.as_view(), name="shop"),
    path("about/", AboutView.as_view(), name="about"),
    path("contact/", ContactView.as_view(), name="contact"),
    path("shop_single/", Shop_SingleView.as_view(), name="shop_single"),

    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogOutView.as_view(), name='logout'),
    path('register/', UserCreateView.as_view(), name='register'),
]
