from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('shuffle.views',
    (r'^$', 'shuffle'),
    (r'^(?P<first>\d+)/check/$', 'check'),
    url(r'^admin/', include(admin.site.urls)),
)
