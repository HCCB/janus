#!/usr/bin/env python
import os.path

from reportlab.lib.styles import ParagraphStyle as PS
from reportlab.platypus import PageBreak
from reportlab.platypus.paragraph import Paragraph
from reportlab.platypus.doctemplate import PageTemplate, BaseDocTemplate
from reportlab.platypus.tableofcontents import TableOfContents
from reportlab.platypus.frames import Frame
from reportlab.lib.units import cm
from reportlab.lib.pagesizes import A5, landscape

from reportlab.platypus.tables import Table, TableStyle

from reportlab.lib.enums import TA_CENTER

from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import black, red

# from reportlab.platypus.flowables import Flowable

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
                      showBoundary=True)

        template = PageTemplate('normal', frames=[frame, ],
                                pagesize=self.pagesize)
        self.loadFonts()
        self.addPageTemplates(template)

    def afterFlowable(self, flowable):
        """Register TOC entries"""
        if flowable.__class__.__name__ == 'Paragraph':
            text = flowable.getPlainText()
            style = flowable.style.name
            if style == 'Heading1':
                self.notify('TOCEntry', (0, text, self.page))
            if style == 'Heading2':
                self.notify('TOCEntry', (1, text, self.page))

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


def masterInfo(doc):
    data = [
        ["Name", "Patient Fullname",
         "Date", "12/12/2016",
         "Case #:", "168698"],
        ["Room #:", "OPD", "Age:", "5", "Gender:", "Female"],
        ["Requesting Physician:", "Dr. Lagare"]
    ]
    # data = [["%X" % (y*16+x) for x in range(12)] for y in range(3)]
    data = [["" for x in range(12)] for y in range(3)]
    styles = getSampleStyleSheet()
    sN = styles["Normal"]
    sN.spaceBefore = 0
    sN.spaceAfter = 2
    # sN.leading = 0
    # Row 1
    data[0][0] = Paragraph("<b>Name:</b><u> Pelicano, Rochelle</u>", sN)
    data[0][6] = Paragraph("<b>Date:</b><u> 06/02/2016</u>", sN)
    data[0][10] = Paragraph("<b>Case #:</b><u> 145591</u>", sN)
    # Row 2
    data[1][0] = Paragraph("<b>Room #:</b><u> OPD</u>", sN)
    data[1][4] = Paragraph("<b>Age:</b><u> 5</u>", sN)
    data[1][8] = Paragraph("<b>Sex:</b><u> Female</u>", sN)
    # Row 3
    data[2][0] = Paragraph("<b>Requesting Physician:</b>" +
                           "<u> Dr. Lagarei</u>", sN)

    width, height = doc.pagesize
    w = width - (doc.leftMargin * 2)
    t = Table(data, colWidths=[w/12]*12)
    t.setStyle(TableStyle([
        ('GRID', (0, 0), (-1, -1), 1, black),
        ('TOPPADDING', (0, 0), (-1, -1), 0),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
        # Row 1
        ('SPAN', (0, 0), (5, 0)),
        ('SPAN', (6, 0), (9, 0)),
        ('SPAN', (10, 0), (11, 0)),
        # Row 2
        ('SPAN', (0, 1), (3, 1)),
        ('SPAN', (4, 1), (7, 1)),
        ('SPAN', (8, 1), (11, 1)),
        # Row 3
        ('SPAN', (0, 2), (11, 2)),
    ]))
    return t


def test():
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
    toc = TableOfContents()

    # header = HeaderFlowable()

    # For conciseness we use the same styles for headings and TOC entries
    toc.levelStyle = [h1, h2]

    width, height = doc.pagesize
    story.append(masterInfo(doc))
    story.append(toc)
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
