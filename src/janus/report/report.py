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

from reportlab.lib.enums import TA_CENTER

from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import red

# from reportlab.platypus.flowables import Flowable

from reportlab.lib.styles import getSampleStyleSheet


class ReportTemplate(BaseDocTemplate):

    def __init__(self, filename, **kw):
        self.allowSplitting = 0
        BaseDocTemplate.__init__(self, filename, **kw)

        self.actualWidth, self.actualHeight = landscape(A5)
        print "self.height:", self.height
        self.topmargin = 2.85 * cm
        self.leftmargin = 0.15 * cm
        self.bottommargin = 0.15*cm

        fh = self.actualHeight - self.topmargin - self.bottommargin
        fw = self.actualWidth - (2 * self.leftmargin)

        frame = Frame(self.leftmargin, self.bottommargin,
                      fw, fh,
                      id='ContentFrame',
                      showBoundary=True)

        template = PageTemplate('normal', frames=[frame, ],
                                pagesize=landscape(A5))
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
        h = self.actualHeight
        self.canv.drawImage(logo, 0.2*cm, h-self.topmargin,
                            height=self.topmargin,
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

        w = self.actualWidth
        h = self.actualHeight
        f = Frame(0, h-self.topmargin, w, self.topmargin,
                  showBoundary=False)
        f.addFromList(story, self.canv)

        self.canv.setStrokeColor(red)
        self.canv.setLineWidth(3)
        self.canv.line(0.15*cm, h-self.topmargin,
                       w-0.15*cm, h-self.topmargin,
                       )

    def normpath(self, filespec):
        path = os.path.dirname(os.path.relpath(__file__))
        return os.path.join(path, filespec)

    def loadFonts(self):
        ttfFile = self.normpath('fonts/oldeng.ttf')
        pdfmetrics.registerFont(TTFont("OldEngMT", ttfFile))


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

    # Build story.
    story = []
    toc = TableOfContents()

    # header = HeaderFlowable()

    # For conciseness we use the same styles for headings and TOC entries
    toc.levelStyle = [h1, h2]

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

    doc = ReportTemplate('mintoc.pdf')
    doc.multiBuild(story)


if __name__ == "__main__":
    import sys
    sys.exit(test())
