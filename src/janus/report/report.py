#!/usr/bin/env python

from reportlab.lib.styles import ParagraphStyle as PS
from reportlab.platypus import PageBreak
from reportlab.platypus.paragraph import Paragraph
from reportlab.platypus.doctemplate import PageTemplate, BaseDocTemplate
from reportlab.platypus.tableofcontents import TableOfContents
from reportlab.platypus.frames import Frame
from reportlab.lib.units import cm
from reportlab.lib.pagesizes import A5, landscape

from reportlab.lib.utils import ImageReader

# from reportlab.platypus.flowables import Flowable

# from reportlab.lib.styles import getSampleStyleSheet


class ReportTemplate(BaseDocTemplate):

    def __init__(self, filename, **kw):
        self.allowSplitting = 0
        BaseDocTemplate.__init__(self, filename, **kw)

        height, width = A5
        print A5
        topmargin = 2.5 * cm
        leftmargin = 2 * cm

        fh = height - (2 * topmargin)
        fw = width - (2 * leftmargin)

        frame = Frame(leftmargin, topmargin, fw, fh, id='ContentFrame',
                      showBoundary=True)

        template = PageTemplate('normal', frames=[frame, ],
                                pagesize=landscape(A5))
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
        import os.path

        c = self.canv
        c.saveState()

        c.drawString(0.2*cm, 0.2*cm, "Hello World")

        path = os.path.dirname(os.path.realpath(__file__))
        logo_fname = os.path.join(path, 'static/HCCB-Hospital-Logo.png')
        logo = ImageReader(logo_fname)
        c.drawImage(logo, 0.2*cm, 0.5*cm, mask='auto')

        c.restoreState()


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
