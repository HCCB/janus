import StringIO
# from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import viewsets
# , permissions
# from reportlab.pdfgen import canvas
from reportlab.platypus.paragraph import Paragraph
from reportlab.lib.styles import ParagraphStyle as PS

from serializers import PatientSerializer
from models import Patient
from reports.reports import ReportTemplate, MasterInfo


class PatientViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows patients to be viewed or edited.
    """
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


def pdf_view(request):
    buff = StringIO.StringIO()

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="report.pdf"'

    doc = ReportTemplate(buff)

    story = []
    story.append(MasterInfo())
    story.append(Paragraph('Text in first heading', PS('body')))

    doc.multiBuild(story)

    response.write(buff.getvalue())
    buff.close()

    return response
