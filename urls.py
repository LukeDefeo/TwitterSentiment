from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
from django.contrib import admin
from views import *

urlpatterns = patterns('',
                       # Examples:
                       url(r'^$', main_page),

                       url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^json$', return_json),
                       url(r'^cleanup/', clean_up),


)
