"""rhOline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path,include,re_path
from apps.organization.views import OrgView
from django.views.static import serve
from rhOline.settings import MEDIA_ROOT
import xadmin

urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('users/', include(('apps.users.urls', "apps.users"), namespace="users")),
    path('captcha/', include('captcha.urls')),
    path('org/', include('organization.urls',namespace='org')),
    re_path(r'^media/(?P<path>.*)', serve, {"document_root": MEDIA_ROOT }),
    path("course/", include('course.urls', namespace="course")),
]


