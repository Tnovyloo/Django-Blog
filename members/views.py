from django.shortcuts import render
from django.views import generic
from django.contrib.auth.views import PasswordChangeView
from .forms import MyUserCreationForm, MyUserAuthenticationForm, MyUserChangeForm, MyPasswordChangeForm
from django.urls import reverse_lazy

class PasswordsChangeView(PasswordChangeView):
    form_class = MyPasswordChangeForm
    template_name = 'registration/change-password.html'
    success_url = reverse_lazy('index')

class UserRegisterView(generic.CreateView):
    form_class = MyUserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

class UserLoginView(generic.CreateView):
    form_class = MyUserAuthenticationForm
    template_name = 'registration/login.html'
    success_url = reverse_lazy('')

class UserEditView(generic.UpdateView):
    form_class = MyUserChangeForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        return self.request.user