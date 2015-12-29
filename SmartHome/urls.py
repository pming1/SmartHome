# coding=utf-8
"""SmartHome URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
# from rest_framework import routers
# from api import views
#
# router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)
# router.register(r'switches', views.SwitchViewSet)

urlpatterns = [
    # url(r'^', include(router.urls)),
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/', include('api.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^wechat', include('wechat.urls', namespace="wechat")),
]

from wiki.urls import get_pattern as get_wiki_pattern
from django_nyt.urls import get_pattern as get_nyt_pattern

urlpatterns += [
    url(r'^wiki/notifications', get_nyt_pattern()),
    url(r'^wiki', get_wiki_pattern())
]

from django.conf import settings
from django.contrib.staticfiles import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += [
        url(r'^static/(?P<path>.*)$', views.serve),
    ]


# urlpatterns = format_suffix_patterns(urlpatterns)
