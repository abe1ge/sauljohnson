from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'frontend.views.index'),
    url(r'contact$', 'frontend.views.contact'),
    url(r'linkedin$', 'frontend.views.linkedin'),
    url(r'privacy$', 'frontend.views.privacy'),
    url(r'terms$', 'frontend.views.terms'),
    url(r'silence$', 'frontend.views.silence'),
    url(r'brainfony$', 'frontend.views.brainfony'),
    url(r'flatfolio$', 'frontend.views.flatfolio'),
    url(r'denobo$', 'frontend.views.denobo'),
    url(r'veryrss$', 'frontend.views.veryrss'),
    url(r'blog$', 'frontend.views.blog'),
    url(r'crisp$', 'frontend.views.crisp'),
    url(r'me-and-the-web$', 'frontend.views.me_and_the_web'),
    url(r'me-and-the-desktop$', 'frontend.views.me_and_the_desktop'),
)
