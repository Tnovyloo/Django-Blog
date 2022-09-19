from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView
# from ..members.forms import MyUserAuthenticationForm
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    # path('login/', LoginView.as_view(authentication_form=MyAuthenticationForm)),
    path('members/', include('django.contrib.auth.urls')),
    path('members/', include('members.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
