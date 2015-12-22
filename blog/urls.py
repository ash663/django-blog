from django.conf.urls import patterns, include, url
from django.contrib import admin
from . import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ashishpatil_in.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^post/(<?P<id>\d{3})', views.post),
    url(r'', views.index),
    #url(r'^accounts/', include('allauth.urls')),

)
