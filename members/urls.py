from django.urls import path, include
from .views import UserRegisterView, UserLoginView, UserEditView, PasswordsChangeView, ShowProfilePageView,\
    EditProfilePageView, CreateProfilePageView
from django.contrib.auth import views as auth_views
from .forms import MyUserAuthenticationForm
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    # path('login/', UserLoginView.as_view(), name='login'),
    path('login/', LoginView.as_view(authentication_form=MyUserAuthenticationForm)),
    path('members/', include('django.contrib.auth.urls')),
    path('<int:pk>/edit_profile/', UserEditView.as_view(), name='edit_profile'),
    # path('password/', auth_views.PasswordChangeView.as_view(template_name='registration/change-password.html'))
    path('password/', PasswordsChangeView.as_view(), name='password'),
    path('<int:pk>/profile', ShowProfilePageView.as_view(), name='show_profile_page'),
    path('<int:pk>/edit_profile_page', EditProfilePageView.as_view(), name='edit_profile_page'),
    path('create_profile_page', CreateProfilePageView.as_view(), name='create_profile_page')
]
