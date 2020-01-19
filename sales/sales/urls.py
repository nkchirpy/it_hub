"""sales URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from employee import views
from django.views.generic.base import TemplateView # new
from django.shortcuts import redirect

# https://wsvincent.com/django-user-authentication-tutorial-login-and-logout/



urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')), # new
    path('', lambda request: redirect('accounts/login/', permanent=False)),
    path('', TemplateView.as_view(template_name='home.html'), name='home'), # new
    path('dashboard',views.Dashboard.as_view(), name='dashboard'),
    path('call/',views.CallView.as_view(), name='call'),
    path('call/<int:pk>/',views.CallView.as_view(), name='call_done'),
    path('engineer/',views.to_do_list, name='engineer'),
    path('engineer/<int:pk>/edit/',views.todo_edit, name='engineer_edit'),
]
