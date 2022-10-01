"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from re import template
from django.contrib import admin
from django.urls import path ,include
from django.conf.urls.static import static
from django.conf import settings

from users import views as user_views
from django.contrib.auth import views as authviews



urlpatterns = [
    path('admin/', admin.site.urls),
    path('core/',include('core.urls')),
    path('register/' ,user_views.register,name='register'),
    path('login/',authviews.LoginView.as_view(template_name='users/login.html'),name='login'),
    path('logout/',authviews.LogoutView.as_view(template_name='users/logout.html'),name='logout'),
    path('profile/',user_views.profile,name='profile'),
    path('passwordreset/',authviews.PasswordResetView.as_view(template_name='users/password_reset.html'),name='passreset'),
    path('passwordreset/Done',authviews.PasswordResetDoneView.as_view(template_name='users/passwordreset_done.html'),name='password_reset_done'),
    path('passwordreset-confirm/<uidb64>/<token>/',authviews.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),name='passwordr_reset_confirm'),


    

    


]
if settings.DEBUG:

  urlpatterns += static(settings.MEDIA_URL, document_root =settings.MEDIA_ROOT)

