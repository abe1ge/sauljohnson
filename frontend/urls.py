from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'frontend.views.index'),
    url(r'contact$', 'frontend.views.contact'),
    url(r'linkedin$', 'frontend.views.linkedin'),
    url(r'privacy$', 'frontend.views.privacy'),
    url(r'terms$', 'frontend.views.terms'),
    url(r'login$', 'frontend.views.login'),
    url(r'silence$', 'frontend.views.silence'),
    url(r'brainfony$', 'frontend.views.brainfony'),
    url(r'flatfolio$', 'frontend.views.flatfolio'),
    url(r'denobo$', 'frontend.views.denobo'),
    url(r'me-and-the-web$', 'frontend.views.me_and_the_web'),
)
