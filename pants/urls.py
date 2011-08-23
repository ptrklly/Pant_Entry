from django.conf.urls.defaults import *
from django.views.generic.edit import CreateView
from pants.models import Pant, Feedback

urlpatterns = patterns('pants.views',
    (r'^$', 'search'),
    (r'^(?P<pant_id>\d+)/$', 'detail'),
    (r'^(?P<pant_id>\d+)/submit/$', 'submit'),
    (r'^thanks/$', 'thanks'),
    url(r'^create/$',CreateView.as_view(model=Pant, success_url="/pants/thanks/"),name="pant_create"),
    url(r'^feedback/$',CreateView.as_view(model=Feedback, success_url="/pants/thanks/"), name="doesitmatter"),
)
