__author__ = 'PmaxLoo'

from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
# router.register(r'hardwares', views.HardwareViewSet)
router.register(r'switches', views.SwitchViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # url(r'^switches/$', views.SwitchList.as_view()),
    url(r'^switches/(?P<pk>[0-9]+)/(?P<action>.+)/$', views.switch_control),
]

# urlpatterns = format_suffix_patterns(urlpatterns)


