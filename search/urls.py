from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('search.views',
    (r'^$', 'results'),
    (r'^thirtytwo/$', 'thirtytwo'),
    (r'^thirtythree/$', 'thirtythree'),
    (r'^thirtyone/$','thirtyone'),
    (r'^eight/$', 'eight'),
    (r'^nine/$', 'nine'),
    (r'^ten/$','ten'),
    (r'^nine/thirtytwo', 'ninethirtytwo'),
    (r'^nine/thirtythree', 'ninethirtythree'),
    (r'^nine/thirtyone', 'ninethirtyone'),
    (r'^twelve/$', 'twelve'),
    (r'^thirteen/$', 'thirteen'),
    (r'^fourteen/$', 'fourteen'),
    (r'^fifteen/$', 'fifteen'),
    (r'^110/$', 'oneten'),
    (r'^111/$', 'oneeleven'),
    (r'^112/$', 'onetwelve'),
    (r'^3310/$', 'looserWlooserA'),
    (r'^339/$', 'looserWsameA'),
    (r'^338/$', 'looserWtighterA'), 
    (r'^3210/$', 'sameWlooserA'),
    (r'^329/$', 'sameWsameA'), 
    (r'^328/$', 'sameWtighterA'),
    (r'^318/$', 'tighterWtighterA'),
    (r'^319/$', 'tighterWsameA'),
    (r'^3110/$', 'tighterWlooserA'),
    url(r'^admin/', include(admin.site.urls)),
)
