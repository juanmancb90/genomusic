from django.conf.urls import patterns, url

urlpatterns = patterns(
    'web.views',
    url(r'^', 'index', name='index'),
    url(r'^sequence/search/', 'search_sequence', name='search_sequence')
)
