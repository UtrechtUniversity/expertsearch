"""webserver URL Configuration

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
from django.conf.urls import include
from django.urls import re_path as url
from queryme import views
#from .query import qry

urlpatterns = [
	url('queryme/search/', views.search),
	url('queryme/search_exp/', views.search_exp),
	url('queryme/search_auth_docs/', views.search_auth_docs),
	url('queryme/recommend', views.recommend),
	url('queryme/domainsearch', views.domainsearch),
	url('queryme/theme', views.theme),
	url('queryme', include('queryme.urls')),
    url('admin/', admin.site.urls),
]
