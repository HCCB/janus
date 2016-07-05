# from django.shortcuts import render

from rest_framework import viewsets
# , permissions

from serializers import PatientSerializer
from models import Patient


class PatientViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows patients to be viewed or edited.
    """
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
