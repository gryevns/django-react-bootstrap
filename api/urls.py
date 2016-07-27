from django.conf.urls import url, include
from api.views import UserViewSet
from rest_framework import routers, renderers

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
	url(r'^', include(router.urls)),
]