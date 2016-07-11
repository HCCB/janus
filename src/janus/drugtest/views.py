# from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import viewsets
# , permissions
from reportlab.pdfgen import canvas

from serializers import PatientSerializer
from models import Patient


class PatientViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows patients to be viewed or edited.
    """
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


def pdf_view(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="report.pdf"'
    p = canvas.Canvas(response)
    p.init_graphics_state()

    p.drawString(100, 100, "Hello world.")

    p.showPage()
    p.save()

    return response
