from django.conf.urls import patterns, include, url

# from django.contrib import admin
from UAM.views import *
# admin.autodiscover()

urlpatterns = patterns('',
   
    url(r'^$', approverlogin),   
    url(r'^approverlogin/',approverlogin),
    # url(r'^admin/', include(admin.site.urls)),
)
