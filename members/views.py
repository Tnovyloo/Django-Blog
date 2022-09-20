from django.shortcuts import render
from django.views import generic
from django.contrib.auth.views import PasswordChangeView
from .forms import MyUserCreationForm, MyUserAuthenticationForm, MyUserChangeForm, MyPasswordChangeForm,\
    UpdateProfileForm, CreateProfileForm
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView, CreateView
from django.contrib.auth.views import LoginView
from core.models import Profile
from django.shortcuts import get_object_or_404

class CreateProfilePageView(CreateView):
    model = Profile
    template_name = 'registration/create_profile_page.html'
    form_class = CreateProfileForm
    success_url = reverse_lazy('index')

    # To sent User into Create profile form while creating profile which needs a User.
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class EditProfilePageView(UpdateView):
    model = Profile
    template_name = 'registration/edit_profile_page.html'
    form_class = UpdateProfileForm
    success_url = reverse_lazy('index')

    def get_context_data(self, *args, **kwargs):
        context = super(EditProfilePageView, self).get_context_data(**kwargs)
        profile_object = get_object_or_404(Profile, id=self.kwargs['pk'])

        context['profile_object'] = profile_object

        return context

class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'registration/user-profile.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ShowProfilePageView, self).get_context_data(**kwargs)
        profile_object = get_object_or_404(Profile, id=self.kwargs['pk'])

        context['profile_object'] = profile_object

        return context

class PasswordsChangeView(PasswordChangeView):
    form_class = MyPasswordChangeForm
    template_name = 'registration/change-password.html'
    success_url = reverse_lazy('index')

class UserRegisterView(CreateView):
    form_class = MyUserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

class UserLoginView(CreateView):
    form_class = MyUserAuthenticationForm
    template_name = 'registration/login.html'
    success_url = reverse_lazy('')

class UserEditView(UpdateView):
    form_class = MyUserChangeForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, *args, **kwargs):
        context = super(UserEditView, self).get_context_data(**kwargs)
        profile_object = get_object_or_404(Profile, id=self.kwargs['pk'])

        context['profile_object'] = profile_object

        return context