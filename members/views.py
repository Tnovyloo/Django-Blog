from django.shortcuts import render
from django.views import generic
from .forms import MyUserCreationForm, MyUserAuthenticationForm
from django.urls import reverse_lazy

class UserRegisterView(generic.CreateView):
    form_class = MyUserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

class UserLoginView(generic.CreateView):
    form_class = MyUserAuthenticationForm
    template_name = 'registration/login.html'
    success_url = reverse_lazy('')
