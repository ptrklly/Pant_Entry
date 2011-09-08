from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('shuffle.views',
    (r'^$', 'shuffle'),
    url(r'^admin/', include(admin.site.urls)),
)
