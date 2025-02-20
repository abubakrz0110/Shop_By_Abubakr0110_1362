from django.shortcuts import render, redirect
from django.views.generic import ListView, TemplateView, CreateView, UpdateView, DeleteView, FormView
from django.views import View
from .models import Users, Product, Banner, Brand
from .forms import UserCreateForm, UserLoginForm
from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


class IndexView(ListView):
    template_name = 'index.html'
    model = Product
    login_url = 'login/'


    content_object_name = 'products'
    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        products = Product.objects.all()
        banner = Banner.objects.all()
        contex['prodacts'] = products
        contex['banner'] = banner
        return contex


class ShopView(ListView):
    template_name = 'shop.html'
    model = Product
    context_object_name = 'products'


class AboutView(TemplateView):
    template_name = 'about.html'



class ContactView(LoginRequiredMixin, ListView):
    model = Brand
    template_name = 'contact.html'
    login_url = reverse_lazy('login')  # Используем имя маршрута


class Shop_SingleView(TemplateView):
    template_name = 'shop-single.html'


class UserCreateView(CreateView):
    model = Users
    form_class = UserCreateForm
    template_name = 'register.html'
    success_url = '/'


class UserLoginView(FormView):
    form_class = UserLoginForm
    template_name = 'login.html'
    success_url = '/'

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = Users.objects.filter(username=username).first()
        print(username, user, password)
        # print(username, user, password)
        if user and user.check_password(password):
            login(self.request, user)
            return redirect('/')
        return super().form_valid(form)


class UserLogOutView(View):
    def get(self, request):
        logout(request)
        return redirect('/')
