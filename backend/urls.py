from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('backend.views',
    (r'^$', 'allpants'),
    (r'^Same waist', 'sameW'),
    (r'^Looser waist', 'looserW'),
    (r'^Tighter waist', 'tighterW'),
    (r'^Same rise', 'sameR'),
    (r'^Lower rise', 'lowerR'),
    (r'^Higher rise', 'higherR'),
    (r'^Slim', 'slim'),
    url(r'^admin/', include(admin.site.urls)),
)
