"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import re_path, include
from django.views.generic import TemplateView
from rest_framework import routers
from user_profile.views import UserViewSet

router = routers.DefaultRouter()
router.register(r'user', UserViewSet,)

urlpatterns = [
    re_path(r'^api/', include(router.urls)),
    re_path(r'^api/', include('users.urls')),

    # Authenticate API Site
    re_path(r'^api-auth/', include('rest_framework.urls')),

    # This is used for user reset password
    re_path(r'^', include('django.contrib.auth.urls')),
    re_path(r'^rest-auth/', include('rest_auth.urls')),
    re_path(r'rest-auth/registration/', include('rest_auth.registration.urls')),
    re_path(r'^account/', include('allauth.urls')),
    re_path(r'^admin/', admin.site.urls),
]
