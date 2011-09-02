from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^accounts/', include('registration.urls')),
    (r'^pants/', include('pants.urls')),
    (r'^profiles/', include('profiles.urls')),
    (r'^$', 'pants.views.login_view'),
    (r'^logout', 'pants.views.logout_view'),
    (r'^outsuccess', 'pants.views.logout_action'),
    (r'^search', 'pants.views.search'),
    (r'^dynamiccatalog', 'pants.views.dynamiccatalog'),
    (r'^about', 'pants.views.about'),
    (r'^staff', 'pants.views.aboutstaff'),
    (r'^press', 'pants.views.press'),
    (r'^findus', 'pants.views.findus'),
    (r'^success', 'pants.views.log_view'),
    (r'^results', 'pants.views.results'),
    (r'^thirtytwo/$', 'pants.views.thirtytwo'),
    (r'^thirtythree/$', 'pants.views.thirtythree'),
    (r'^thirtyone/$','pants.views.thirtyone'),
    (r'^eight/$', 'pants.views.eight'),
    (r'^nine/$', 'pants.views.nine'),
    (r'^ten/$', 'pants.views.ten'),
    (r'^nine/thirtytwo', 'pants.views.thirty'),
    url(r'^admin/', include(admin.site.urls)),
)
