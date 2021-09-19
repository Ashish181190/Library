"""Library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
import abc
from subscribe.forms import Subscribe

from Book.views import *
from django.contrib import admin
from django.urls import path
from subscribe.views import subscribe_email

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('home/', func),
    path('homepage/', homepage, name = "home"),
    path('show-books/', get_book, name = "showbook"),
    path('Update-books/ <int:id>/', Update_book, name = "update"),
    path('soft-Delete/ <int:id>/', soft_delete, name = "soft_delete"),
    path('hard-Delete/ <int:id>/', hard_delete, name = "hard_delete"),
    path('Active_book/', active_book, name = "active_books"),
    path('In_Active_book/', in_active_book, name = "in_active_books"),
    path('Restore_book/ <int:id>/', restore, name = "restore"),
    path('email-home/', subscribe_email, name = 'Subscribe' )

]
