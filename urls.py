from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
from django.contrib import admin
from views import *

urlpatterns = patterns('',
    # Examples:
     url(r'^$', main_page),
    # url(r'^Django_Test/', include('Django_Test.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^tweet/(\w{1,100})/$', test_json),
        url(r'^json$', return_json)



)
