"""
URL configuration for ToDoList project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from tasks.views import *

urlpatterns = [
    path('task_list/', task_list, name="task_list"),
    path('add_task/', add_task , name="add_task"),
    path('delete_task/<int:task_id>/', delete_task , name="delete_task"),
    path('toggle_task/<int:task_id>/', toggle_task , name="toggle_task"), 
    path('login_page/', login_page , name="login_page"), 
    path('logout/', logout, name="logout"), 
    path('register_page/', register_page , name="register_page"),   
       
    path('admin/', admin.site.urls),
    
]
