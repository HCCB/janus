from io import BytesIO
# import datetime

# from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import viewsets
# , permissions
# from reportlab.pdfgen import canvas
from reportlab.platypus.paragraph import Paragraph
from reportlab.lib.styles import ParagraphStyle as PS
from reportlab.platypus import PageBreak as BR

from serializers import PatientSerializer
from models import Patient
from models import ResultMaster
from reports.reports import ReportTemplate, MasterInfo


class PatientViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows patients to be viewed or edited.
    """
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


def pdf_view(request):

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="report.pdf"'

    raw = generate_pdf()

    response.write(raw)

    return response


def generate_pdf():

    m = ResultMaster.objects.first()
    # p = m.patient

    buff = BytesIO()
    try:
        doc = ReportTemplate(buff)

        story = []
        story.append(MasterInfo(
            # patient=p,
            # date=datetime.datetime.now(),
            # room_no='OPD',
            # case_no='1234567890',
            # physician='Dr. Doctor',
            master=m,
            # fullname='blue cuenca',
        ))
        story.append(Paragraph(m.title, PS('H1')))
        story.append(Paragraph('Text in first heading', PS('body')))

        story.append(BR())

        story.append(MasterInfo(master=m))
        story.append(Paragraph('Next one', PS('body')))
        doc.multiBuild(story)

        buff.flush()
        raw_value = buff.getvalue()
    finally:
        buff.close()

    return raw_value
