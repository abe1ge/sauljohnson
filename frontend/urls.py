from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'frontend.views.index'),
    url(r'contact$', 'frontend.views.contact'),
    url(r'linkedin$', 'frontend.views.linkedin'),
    url(r'privacy$', 'frontend.views.privacy'),
    url(r'terms$', 'frontend.views.terms'),
    url(r'login$', 'frontend.views.login'),
)
