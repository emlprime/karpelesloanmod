from django.conf.urls.defaults import *

from django.contrib import admin

admin.autodiscover()

from karpelesloanmod.settings import MEDIA_ROOT

urlpatterns = patterns('',
    (r'^admin/(.*)$', admin.site.root),
    (r'^site_media/(.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT}),
)

urlpatterns += patterns('karpelesloanmod.content.views',
    (r'^$', 'loan_modifications'),
)

urlpatterns += patterns('django.views.generic.simple',
    (r'^site_map/$', 'direct_to_template', {'template':'site_map.html'}),
)
