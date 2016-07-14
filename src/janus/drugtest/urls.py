from django.conf.urls import url, include

from rest_framework import routers

import views


router = routers.DefaultRouter()

router.register(r'patient', views.PatientViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^testpdf/$', views.pdf_view, name='pdftest'),
]
