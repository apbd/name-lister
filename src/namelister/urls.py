"""namelister URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from names.views import names_view, upload_view #sort_names, sort_amount

urlpatterns = [
    path('admin/', admin.site.urls),

    # names view
    path('names/', names_view, name="home"),
    path('names/sort-by-name/', names_view, name="sortnames"),
    path('names/sort-by-amount/', names_view, name="sortamount"),

    # upload view
    path('upload/', upload_view, name="upload"),


]
