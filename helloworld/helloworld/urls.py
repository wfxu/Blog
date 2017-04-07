from django.conf.urls import *
from django.contrib import admin
from helloworld.view import hello
from helloworld.testdb import testdb
from helloworld import search
from helloworld import search2

admin.autodiscover()
#urlpatterns=[url('^hello/$',hello),]
urlpatterns = [  
    url('^hello/$', hello), 
    url('^testdb/$',testdb), 
    url('^search-form/$',search.search_form),
    url('^search/$',search.search),
    url('^search-post/$',search2.search_post),
    url(r'^admin/',include(admin.site.urls)),
]  
