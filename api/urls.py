from django.conf.urls import url, include
from api.views import UserViewSet
from rest_framework import routers, renderers
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^obtain-auth-token/$', obtain_auth_token)
]