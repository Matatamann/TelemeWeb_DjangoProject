"""untitled URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from home import views

urlpatterns = [
    url(r'^developer/', 'home.views.developer'),
    url(r'^fuel/', 'home.views.fuel'),
    url(r'^gps/', 'home.views.gps'),
    url(r'^$', 'home.views.index'),
    url(r'^positions/', 'home.views.positions'),
    url(r'^rpm/', 'home.views.rpm'),
    url(r'^temperature/', 'home.views.temperature'),
    url(r'^trail/', 'home.views.trail'),
    url(r'^velocity/', 'home.views.velocity'),
    url(r'^charts/', include('charts.urls')),
    url(r'^admin/', admin.site.urls),
]
