from django.conf.urls import url, include

from rest_framework import routers

import views


router = routers.DefaultRouter()

router.register(r'person', views.PersonViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
]
