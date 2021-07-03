"""vc URL Configuration

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
from django.contrib import admin
from django.urls import path
from api import  views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/list',views.StudentList.as_view()),
    path('api/re/<int:pk>',views.StudentRe.as_view()),
    path('api/up/<int:pk>',views.StudentUp.as_view()),
    path('api/de/<int:pk>',views.StudentDe.as_view()),

    # combine stared
    path('api/lc',views.StudenLC.as_view()),
    path('api/ru/<int:pk>',views.StudenRU.as_view()),
    path('api/rd/<int:pk>', views.StudenRD.as_view()),
    # for three class
    path('api/rud/<int:pk>', views.StudenRUD.as_view()),

    # if you only want to do CRUD operation use only two classes i.e RetrieveUpdateDestroyAPIView and ListCreateAPIView
    path('api/all',views.StudentLC.as_view()),
    path('api/all/<int:pk>', views.StudentRUD.as_view()),
]
