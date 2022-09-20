from django.urls import path
from .views import UserRegisterView, UserLoginView, UserEditView, PasswordsChangeView, ShowProfilePageView
# from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
    # path('password/', auth_views.PasswordChangeView.as_view(template_name='registration/change-password.html'))
    path('password/', PasswordsChangeView.as_view(), name='password'),
    path('<int:pk>/profile', ShowProfilePageView.as_view(), name='show_profile_page'),
]
