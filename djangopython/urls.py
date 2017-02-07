"""djangopython URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from front import views as front_views

urlpatterns = [
    url ( r'^$', front_views.home, name = 'home' ),
    url ( r'^index/$', front_views.index ),
    url ( r'^add/$', front_views.add, name = 'add' ),
    url ( r'^addredirect/(\d+)/(\d+)/$', front_views.oldAddRedirect, name = 'addredirect' ),
    url ( r'^addparams/$', front_views.addparams, name = 'addparams' ),
    # url ( r'^addparams/(\d+)/(\d+)/$', front_views.addparams, name = 'addparams' ),
    url ( r'^(\d+)/addparams_new/(\d+)/$', front_views.addparams, name = 'addparams' ),
    # url ( r'^(\d+)_addparams_new/(\d+)/$', front_views.addparams, name = 'addparams' ),
    url ( r'^learntemplate/$', front_views.learnTemplate, name = 'learn_template' ),
    url ( r'^learnqueryset/$', front_views.learnQueryset, name = 'learn_queryset' ),
    url ( r'^admin/', admin.site.urls ),
]
