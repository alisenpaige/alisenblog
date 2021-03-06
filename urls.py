from django.conf.urls.defaults import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from blog.views import LatestPostFeed

urlpatterns = patterns('',
    # Example:
    (r'^blog[/]', include('alisenblog.log.urls')),
    (r'^', include('alisenblog.site.urls')),

    #Feed
    url(r'^feed/$',
        LatestPostFeed(),
        name='feed',
        ),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
    (r'^static/alisen/(?P<path>.*)$',
        'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    )

