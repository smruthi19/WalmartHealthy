"""healthyfoods URL Configuration

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
from myapp import views
from django.urls import path
from django.conf.urls import url
from django.views.static import serve
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^checkout/', views.checkout, name='checkout'),
    url(r'^category/', views.category, name='category'),
    url(r'^cart/', views.cart, name='cart'),
    url(r'^fruits/', views.fruits, name='fruits'),
    url(r'^specificcart/', views.specificcart, name='specificcart'),
    url(r'^fruitcart/', views.fruitcart, name='fruitcart'),
    # url(r'^page3/', views.webpage3, name='webpage3'),
    # url(r'^contact/', views.contact, name='contact'),
    url(r'^about/', views.about, name='about'),
    url(r'^blog/', views.blog, name='blog'),
    url(r'^dairy/', views.dairy, name='dairy'),
    url(r'^dairycart/', views.dairycart, name='dairycart'),
    url(r'^drinkcart/', views.drinkcart, name='drinkcart'),
    url(r'^drink/', views.drink, name='drink'),
    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]
