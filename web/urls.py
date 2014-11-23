from django.conf.urls import patterns, url

urlpatterns = patterns(
    'web.views',
    url(r'^', 'index', name='index'),
    url(r'^sequence/get/', 'get_sequence', name='get_sequence')
)
