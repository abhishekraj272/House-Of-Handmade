"""myproject URL Configuration

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
from django.urls import path
from .views import home_page
from HandiCraft.views import (login_page,signup_page,scarfs_page,socks_page,earrings_page,sweaters_page,vases_page,recover_page,terms_page,sweater_detail_page,scarf_detail_page,vase_detail_page,socks_detail_page,earring_detail_page)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page),
    path('login/', login_page),
    path('signup/', signup_page),
    path('sweaters/', sweaters_page),
    path('vases/', vases_page),
    path('scarfs/', scarfs_page),
    path('earrings/',earrings_page),
    path('socks/',socks_page),
    path('recover/',recover_page),
    path('termsandconditions/',terms_page),
    path('sweater-details/',sweater_detail_page),
    path('scarf-details/',scarf_detail_page),
    path('socks-details/',socks_detail_page),
    path('vase-details/',vase_detail_page),
    path('earring-details/',earring_detail_page),
]
