"""library_management_system URL Configuration

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
from django.contrib import admin
from django.urls import path,include
from .import views
urlpatterns = [

    path('',views.index,name = 'index'),
    path('Get_all_book',views.Add_a_book,name = 'Get all book'),
    path('Add_a_book',views.Add_a_book,name = 'Add book'),
    path('Delete_a_book',views.Delete_a_book,name = 'Delete book'),
    path('Delete_a_book/<int:book_code=0>',views.Delete_a_book,name = 'Delete book'),
    path('Update_an_entry_of_book',views.Update_an_entry_of_a_book,name = 'Update book entry'),


]