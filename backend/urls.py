from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('backend.views',
    (r'^$', 'prototypeA'),
    (r'prototypeA/$', 'prototypeA'),
    (r'^Same waist/$', 'sameW'),
    (r'^Looser waist/$', 'looserW'),
    (r'^Tighter waist/$', 'tighterW'),
    (r'^Same rise/$', 'sameR'),
    (r'^Lower rise/$', 'lowerR'),
    (r'^Higher rise/$', 'higherR'),
    (r'^Same waist/Same rise/$', 'sWsR'),
    (r'^Same waist/Lower rise/$', 'sWlR'),
    (r'^Same waist/Higher rise/$', 'sWhR'),
    (r'^Looser waist/Same rise/$', 'lWsR'),
    (r'^Looser waist/Lower rise/$', 'lWlR'),
    (r'^Looser waist/Higher rise/$', 'lWhR'),
    (r'^Tighter waist/Same rise/$', 'tWsR'),
    (r'^Tighter waist/Lower rise/$', 'tWlR'),
    (r'^Tighter waist/Higher rise/$', 'tWhR'),
    (r'^Higher rise/Looser waist/$', 'lWhR'),
    (r'^Higher rise/Looser waist/$', 'lWhR'),
    (r'^Higher rise/Same waist/$', 'sWhR'),
    (r'^Higher rise/Tighter waist/$', 'tWhR'),
    (r'^Same rise/Looser waist/$', 'lWhR'),
    (r'^Same rise/Same waist/$', 'sWhR'),
    (r'^Same rise/Tighter waist/$', 'tWhR'),
    (r'^Lower rise/Looser waist/$', 'lWhR'),
    (r'^Lower rise/Same waist/$', 'sWhR'),
    (r'^Lower rise/Tighter waist/$', 'tWhR'),
    (r'^Slim', 'slim'),
    url(r'^admin/', include(admin.site.urls)),
)
