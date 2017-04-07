"""wfxu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from . import home, message, blog

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home.hello),
    url(r'^log$', home.log),
    url(r'^about$',home.about),
    url(r'^blog$', blog.blog_list),
    url(r'^blog/page/(.+)$',blog.blog_list_page),
    url(r'^blog/(.+)$', blog.blog_con),
    url(r'^category/(.+)$', blog.blog_category),
    url(r'^time/(.+)$', blog.blog_time),
    url(r'^search$', blog.blog_search),
]
