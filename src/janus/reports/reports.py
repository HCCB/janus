#!/usr/bin/env python
import os.path
import datetime
from itertools import chain
from io import BytesIO

from reportlab.lib.styles import ParagraphStyle as PS
from reportlab.platypus import PageBreak
from reportlab.platypus.paragraph import Paragraph
from reportlab.platypus.doctemplate import PageTemplate, BaseDocTemplate
from reportlab.platypus.frames import Frame
from reportlab.lib.units import cm
from reportlab.lib.pagesizes import A5, landscape

from reportlab.platypus.tables import Table, TableStyle

from reportlab.lib.enums import TA_CENTER, TA_LEFT

from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import black, red

from reportlab.platypus.flowables import Flowable

from reportlab.lib.styles import getSampleStyleSheet


class ReportTemplate(BaseDocTemplate):

    def __init__(self, filename, **kw):
        self.allowSplitting = 0

        self.pagesize = kw.get('pagesize', landscape(A5))
        kw['pagesize'] = self.pagesize

        BaseDocTemplate.__init__(self, filename, **kw)

        w, h = self.pagesize

        # self.actualWidth, self.actualHeight = landscape(A5)
        self.topMargin = 2.85 * cm
        self.leftMargin = 0.15 * cm
        self.bottomMargin = 0.15 * cm

        fh = h - self.topMargin - self.bottomMargin
        fw = w - (2 * self.leftMargin)

        frame = Frame(self.leftMargin, self.bottomMargin,
                      fw, fh,
                      id='ContentFrame',
                      showBoundary=False)

        template = PageTemplate('normal', frames=[frame, ],
                                pagesize=self.pagesize)
        self.loadFonts()
        self.addPageTemplates(template)

    def beforePage(self):
        self.canv.saveState()

        self.drawHeader()

        self.canv.restoreState()

    def drawLogo(self):
        logo_fname = self.normpath('static/HCCB-Hospital-Logo.png')
        logo = ImageReader(logo_fname)
        w, h = self.pagesize
        self.canv.drawImage(logo, 0.2*cm, h-self.topMargin,
                            height=self.topMargin,
                            mask='auto',
                            preserveAspectRatio=True
                            )

    def drawHeader(self):
        self.drawLogo()
        styles = getSampleStyleSheet()
        sN = styles['Normal']
        sH = styles['Heading1']

        sH.fontName = "OldEngMT"
        sH.textColor = red
        sH.leading = 18
        sH.fontSize = 16

        sN.fontSize = 9
        sN.leading = 10

        sN.alignment = sH.alignment = TA_CENTER
        sN.spaceBefore = sH.spaceBefore = 0
        sN.spaceAfter = sH.spaceAfter = 0

        story = []
        story.append(Paragraph("Holy Child Colleges of Butuan - Hospital", sH))
        story.append(Paragraph("<b>(JP Esteves Clinical Laboratory)</b>", sN))
        story.append(Paragraph("2nd St., Guingona Subd., " +
                               "Butuan City, Philippines", sN))
        story.append(Paragraph("Tel. No.: +63 (85) 342-5186", sN))
        story.append(Paragraph("Telefax No.: +63 (95) 342-397/225-6872", sN))
        story.append(Paragraph("email: hccb.hospital@gmail.com", sN))

        w, h = self.pagesize
        f = Frame(0, h-self.topMargin, w, self.topMargin,
                  showBoundary=False)
        f.addFromList(story, self.canv)

        self.canv.setStrokeColor(red)
        self.canv.setLineWidth(3)
        self.canv.line(0.15*cm, h-self.topMargin,
                       w-0.15*cm, h-self.topMargin,
                       )

    def normpath(self, filespec):
        path = os.path.dirname(os.path.relpath(__file__))
        return os.path.join(path, filespec)

    def loadFonts(self):
        ttfFile = self.normpath('fonts/oldeng.ttf')
        pdfmetrics.registerFont(TTFont("OldEngMT", ttfFile))


class MasterInfo(Flowable):
    KEYS = {
        'master': ['patient', 'date', 'room_number',
                   'case_number', 'physician'],
        'patient': ['fullname', 'age', 'gender'],
    }

    def process_kwarg(self, data, kwargs):
        for objname in self.KEYS.keys():
            if objname in kwargs.keys():
                o = kwargs[objname]
                for k in self.KEYS[objname]:
                    display = 'get_%s_display' % k
                    if hasattr(o, display):
                        data[k] = getattr(o, display)()
                    else:
                        data[k] = getattr(o, k)
                del kwargs[objname]

        p = data.get('patient', None)
        for k in chain(*self.KEYS.values()):
            if k in kwargs.keys():
                data[k] = kwargs[k]
                del kwargs[k]
            elif p and hasattr(p, k):
                display = 'get_%s_display' % k
                if hasattr(p, display):
                    data[k] = getattr(p, display)()
                else:
                    data[k] = getattr(p, k)

    def __init__(self, **kwargs):
        data = {}
        self.process_kwarg(data, kwargs)

        self.config = {}
        for k in ['font', 'fontsize', 'offset', 'width',
                  'leftmargin', 'rightmargin']:
            if k in kwargs:
                # setattr(self, k, kwargs[k])
                self.config[k] = kwargs[k]
                del kwargs[k]

        if len(kwargs):
            raise TypeError("__init__ got an unxepected keyworkd '%s'" %
                            kwargs.keys()[0])
        self.init_table(data)

    def init_table(self, data):

        styles = getSampleStyleSheet()
        sN = styles['Normal']
        if 'font' in self.config:
            sN.fontName = self.config['font']
        if 'fontsize' in self.config:
            sN.fontSize = self.config['fontsize']
            sN.leading = sN.fontSize * 1.1

        cell_data = [["" for x in range(12)] for y in range(3)]
        # Row 1
        cell_data[0][0] = Paragraph("<b>Name:</b><u> %s</u>" %
                                    data.get('fullname', 'NO_VALUE'),
                                    sN)
        date_type = type(data['date'])
        if date_type in [datetime.datetime, datetime.date]:
            date = datetime.datetime.strftime(data['date'], "%m/%d/%Y")
        else:
            date = data['date']
        cell_data[0][6] = Paragraph("<b>Date:</b><u> %s</u>" %
                                    date,
                                    sN)
        cell_data[0][9] = Paragraph("<b>Case #:</b><u> %s</u>" %
                                    data.get('case_number', 'NO_VALUE'),
                                    sN)
        # Row 2
        cell_data[1][0] = Paragraph("<b>Room #:</b><u> %s</u>" %
                                    data.get('room_number', 'NO_VALUE'),
                                    sN)
        cell_data[1][4] = Paragraph("<b>Age:</b><u> %s</u>" %
                                    data['age'],
                                    sN)
        cell_data[1][8] = Paragraph("<b>Sex:</b><u> %s</u>" %
                                    data.get('gender', 'NO_VALUE'),
                                    sN)
        # Row 3
        cell_data[2][0] = Paragraph("<b>Requesting Physician:</b><u> %s</u>" %
                                    data.get('physician', 'NO_VALUE'),
                                    sN)
        if 'width' in self.config:
            width = self.config['width']
        else:
            width, height = landscape(A5)
            self.config['width'] = width

        lm = self.config.get('leftmargin', 10)
        rm = self.config.get('rightmargin', 10)
        width -= lm + rm

        self.table = Table(cell_data, colWidths=[width/12]*12)
        self.table.setStyle(TableStyle([
            # ('GRID', (0, 0), (-1, -1), 1, black),
            ('TOPPADDING', (0, 0), (-1, -1), 0),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
            ('BOTTOMPADDING', (0, -1), (0, -1), 3),
            ('LINEBELOW', (0, -1), (-1, -1), 1, black),
            # Row 1
            ('SPAN', (0, 0), (5, 0)),
            ('SPAN', (6, 0), (8, 0)),
            ('SPAN', (9, 0), (11, 0)),
            # Row 2
            ('SPAN', (0, 1), (3, 1)),
            ('SPAN', (4, 1), (7, 1)),
            ('SPAN', (8, 1), (11, 1)),
            # Row 3
            ('SPAN', (0, 2), (11, 2)),
        ]))

    def split(self, availWidth, availHeight):
        return []

    def wrap(self, availWidth, availHeight):
        width, height = self.table.wrap(availWidth, availHeight)
        return (width, height)

    def drawOn(self, canvas, x, y, _sW=0):
        return self.table.drawOn(canvas, x, y, _sW)


class Signatories(Flowable):
    def __init__(self, master, margin=10):
        Flowable.__init__(self)
        self.master = master
        self.margin = 10
        if master.medical_technologist or master.pathologist:
            self.has_data = True
        else:
            self.has_data = False

    def split(self, availWidth, availHeight):
        return []

    def wrap(self, availWidth, availHeight):
        return self.do_table_wrap(availWidth, availHeight)

    def do_table_wrap(self, availWidth, availHeight):
        styles = getSampleStyleSheet()
        sN = styles['Normal']
        sN.alignment = TA_CENTER
        data = [["" for x in range(12)] for y in range(3)]

        data[0][1] = Paragraph("<br/><br/><strong>%s</strong>" %
                               self.master.pathologist.fullname, sN)
        data[1][1] = Paragraph(self.master.pathologist.
                               get_designation_display(), sN)
        data[2][1] = Paragraph("PRC LIC #: %s" %
                               self.master.pathologist.license, sN)

        data[0][7] = Paragraph("<br/><br/><br/><strong>%s</strong>" %
                               self.master.medical_technologist.fullname, sN)
        data[1][7] = Paragraph(self.master.medical_technologist.
                               get_designation_display(), sN)
        data[2][7] = Paragraph("PRC LIC #: %s" %
                               self.master.medical_technologist.license, sN)

        w = availWidth - self.margin * 2
        spacer = int(w / 10)
        remWidth = (w - (spacer * 4)) / 8
        colWidths = [spacer] + \
            [remWidth] * 4 + \
            [spacer] * 2 + \
            [remWidth] * 4 + \
            [spacer]
        self.table = Table(data, colWidths=colWidths)
        self.table.setStyle(TableStyle([
            # config padding
            ('TOPPADDING', (0, 0), (-1, -1), 0),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
            # lines
            ('LINEBELOW', (1, 0), (4, 0), 1, black),
            ('LINEBELOW', (7, 0), (10, 0), 1, black),
            # ('GRID', (0, 0), (-1, -1), 1, black),
            # Column 1
            ('SPAN', (1, 0), (4, 0)),
            ('SPAN', (1, 1), (4, 1)),
            ('SPAN', (1, 2), (4, 2)),
            # Column 2
            ('SPAN', (7, 0), (10, 0)),
            ('SPAN', (7, 1), (10, 1)),
            ('SPAN', (7, 2), (10, 2)),
        ]))
        self.table.canv = self.canv
        return self.table.wrap(availWidth, availHeight)

    def draw(self):
        self.table.draw()


class Grid(Flowable):
    pass


class Report(object):
    def __init__(self, master):
        super(Report, self).__init__()
        self.master = master
        self.styles = getSampleStyleSheet()

    def rows(self):
        for row in self.master.resultdetail_set.all():
            result_list = row.result.split(',')
            component_list = row.analysis.components.split(',')
            ref_list = row.analysis.reference_text.split(',')
            txt = row.analysis.name
            s2 = self.styles['Heading2']
            s2.alignment = TA_CENTER

            sN = self.styles['Normal']
            sN.alignment = TA_LEFT
            yield Paragraph(txt, self.styles['Heading2'])
            for idx, component in enumerate(component_list):
                if ref_list[idx]:
                    txt = '%s: %s (%s)' % (component,
                                           result_list[idx],
                                           ref_list[idx])
                else:
                    txt = '%s: %s' % (component, result_list[idx])
                    sN.alignment = TA_CENTER
                yield Paragraph(txt, sN)
            yield Signatories(self.master)

    def render(self):
        buff = BytesIO()
        try:
            doc = ReportTemplate(buff)
            styles = self.styles
            story = []

            story.append(MasterInfo(master=self.master))
            story.append(Paragraph(self.master.title, styles['Title']))

            for row in self.rows():
                story.append(row)

            doc.multiBuild(story)
            buff.flush()

            raw_value = buff.getvalue()
        finally:
            buff.close()

        return raw_value


def test():
    r = Report(None)
    print r
    h1 = PS(name='Heading1',
            fontSize=14,
            leading=16
            )
    h2 = PS(name='Heading2',
            fontSize=12,
            leading=14,
            leftIndent=1*cm
            )

    doc = ReportTemplate('mintoc.pdf')
    # Build story.
    story = []

    story.append(
        MasterInfo(
            fullname='Full Name',
            case_number='1234567',
            room_number='OPD',
            age='23',
            gender='F',
            date=datetime.datetime.today().date(),
            leftmargin=10,
            rightmargin=10,
        ))
    story.append(PageBreak())
    story.append(Paragraph('First heading', h1))
    story.append(Paragraph('Text in first heading', PS('body')))
    story.append(Paragraph('First sub heading', h2))
    story.append(Paragraph('Text in first sub heading', PS('body')))
    story.append(PageBreak())
    story.append(Paragraph('Second sub heading', h2))
    story.append(Paragraph('Text in second sub heading', PS('body')))
    story.append(Paragraph('Last heading', h1))
    # story.append(header)

    doc.multiBuild(story)


if __name__ == "__main__":
    import sys
    sys.exit(test())
