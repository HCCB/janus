# from django.shortcuts import render

from rest_framework import viewsets

from serializers import PersonSerializer
from models import Person


class PersonViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows persons to be viewed or edited.
    """
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
