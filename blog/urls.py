from django.conf.urls.defaults import *
#from django.http import HttpResponseRedirect
#redirect_to
import models

urlpatterns = patterns('',
    #===========================================================================
    #
    #  Blog Pages 
    #
    #===========================================================================
    #Root blog page
    url(r'^$',
        'blog.views.blog',
        name='blog',
        ),
    
    #Specific blog page
    url(r'^page/(?P<current_page>\d{1,3})/$',
        'blog.views.blog',
        ),

    #url(r'^page/(?P<current_page>\d{1,3})$',
    #    HttpResponseRedirect('/blog/page/(?P<current_page>\d{1,3})/')
    #    ),

    #Get a single blog post
    url(r'^(?P<category>[^/]+)/(?P<filter_value>[^/]+)[/]$',
        'blog.views.blog',
        {
        'query_type': 'single',
        }),

    #===========================================================================
    #   CATEGORIES 
    #===========================================================================
    #Get posts by category
    url(r'^(?P<filter_value>[^/]+)[/]$',
        'blog.views.blog',
        {
        'filter_type': 'category',
        'filter_col': 'slug',
        }),

    #===========================================================================
    #   TAGS
    #===========================================================================
    #Get a list of blog posts by tag
    url(r'^by/tag/(?P<filter_value>[^/]+)[/]$',
        'blog.views.blog',
        {
        'query_type': 'tag',
        'filter_type': 'tags',
        'filter_col': 'slug',
        }),
)
