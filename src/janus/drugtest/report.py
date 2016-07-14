#!/usr/bin/env python

from reportlab.lib.styles import ParagraphStyle as PS
from reportlab.platypus import PageBreak
from reportlab.platypus.paragraph import Paragraph
from reportlab.platypus.doctemplate import PageTemplate, BaseDocTemplate
from reportlab.platypus.tableofcontents import TableOfContents
from reportlab.platypus.frames import Frame
from reportlab.lib.units import cm, inch

from reportlab.platypus.flowables import Flowable

# from reportlab.lib.styles import getSampleStyleSheet


class HeaderFlowable(Flowable):
    '''A Header Flowable'''
    curves = [
        (0,    2), (0,    4), (0,    8),    # back of hand
        (5,    8), (7,   10), (7,   14),
        (10,  14), (10,  13), (7.5,  8),    # thumb
        (13,   8), (14,   8), (17,   8),
        (19,   8), (19,   6), (17,   6),
        (15,   6), (13,   6), (11,   6),    # index, pointing
        (12,   6), (13,   6), (14,   6),
        (16,   6), (16,   4), (14,   4),
        (13,   4), (12,   4), (11,   4),    # middle
        (11.5, 4), (12,   4), (13,   4),
        (15,   4), (15,   2), (13,   2),
        (12.5, 2), (11.5, 2), (11,   2),    # ring
        (11.5, 2), (12,   2), (12.5, 2),
        (14,   2), (14,   0), (12.5, 0),
        (10,   0), (8,    0), (6,    0),    # pinky, then close
    ]

    def __init__(self):
        # from reportlab.lib.units import inch
        from reportlab.lib.colors import tan, green
        self.size = 4 * inch
        self.fillcolor = tan
        self.strokecolor = green
        self.xoffset = 0
        self.scale = inch * 0.2

    def wrap(self, *args):
        return (self.xoffset, self.size)

    def draw(self):
        canvas = self.canv
        canvas.setLineWidth(6)
        canvas.setFillColor(self.fillcolor)
        canvas.setStrokeColor(self.strokecolor)
        canvas.translate(self.xoffset+self.size, 0)
        canvas.rotate(90)
        canvas.scale(self.scale, self.scale)
        self.drawHand()

    def drawHand(self):
        p = self.canv.beginPath()
        p.moveTo(0, 0)
        ccopy = list(self.curves)
        u = self.scale
        while ccopy:
            [(x1, y1), (x2, y2), (x3, y3)] = ccopy[:3]
            del ccopy[:3]
            p.curveTo(x1*u, y1*u, x2*u, y2*u, x3*u, y3*u)
        p.close()
        self.canv.drawPath(p, fill=self.fillcolor)


class ReportTemplate(BaseDocTemplate):

    def __init__(self, filename, **kw):
        self.allowSplitting = 0
        BaseDocTemplate.__init__(self, filename, **kw)
        template = PageTemplate('normal', [Frame(2.5*cm,
                                                 2.5*cm,
                                                 15*cm,
                                                 25*cm,
                                                 id='F1')])
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

    header = HeaderFlowable()

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
    story.append(header)

    doc = ReportTemplate('mintoc.pdf')
    doc.multiBuild(story)


if __name__ == "__main__":
    import sys
    sys.exit(test())
