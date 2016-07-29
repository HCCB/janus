#!/usr/bin/env python
from io import BytesIO

from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import A5, landscape
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import black, red

inch = INCH = 72
cm = CM = inch / 2.54
Courier = 'Courier'
Helvetica = 'Helvetica'
Helvetica_Bold = 'Helvetica-Bold'
Helvetica_Oblique = 'Helvetica-Bold-Oblique'

OldEnglish = "OldEngMT"

Images = [
    (
        './static/HCCB-Hospital-Logo.png',
        0.2 * cm,   # left
        0.2 * cm,   # top
        2.85 * cm,  # height
        'auto',     # mask
        True,       # preserveAspectRatio
    )
]

HX = 5 * inch

oldeng_16_text = [
    (HX, 1.00 * cm, 'CENTER', red,
     "Holy Child Colleges of Butuan - Hospital"),
]
helvetica_bold_9_text = [
    (HX, 1.35 * cm, 'CENTER', black,
     "(JP Esteves Clinical Laboratory)"),
]
helvetica_9_text = [
    (HX, 1.70 * cm, 'CENTER', black,
     "2nd Str., Guingona Subd., Butuan City, Philippines"),
    (HX, 2.05 * cm, 'CENTER', black,
     "Tel. No.: +63 (85) 342-5186"),
    (HX, 2.40 * cm, 'CENTER', black,
     "Telefox No.: +63 (95) 342-3975/225-6872"),
    (HX, 2.75 * cm, 'CENTER', black,
     "email: hccb.hospital@gmail.com"),
]
Labels = {
    (OldEnglish, 16): oldeng_16_text,
    (Helvetica_Bold, 9): helvetica_bold_9_text,
    (Helvetica, 9): helvetica_9_text,
}


# load fonts
ttfFile = './fonts/oldeng.ttf'
pdfmetrics.registerFont(TTFont("OldEngMT", ttfFile))


class BaseForm(object):
    def __init__(self, **kw):
        super(BaseForm, self).__init__()

        self.buff = BytesIO()
        self.verbose = kw.get('verbose', 0)
        self.text_font = kw.get('fontface', Courier)

        self.log("creating canvas")
        self.canvas = Canvas(self.buff)
        pagesize = kw.get("pagesize", landscape(A5))
        self.width, self.height = pagesize

        self.log("pagesize = %s" % str(pagesize))
        self.canvas.setPageSize(pagesize)

        self.__draw_images()

        self.__draw_text_labels()

    def __draw_images(self):
        for img, x, y, h, mask, aspect in Images:
            self.log("opening image - %s" % img)
            self.canvas.drawImage(img, x, self.height - h - y,
                                  height=h,
                                  mask=mask, preserveAspectRatio=aspect)

    def __draw_text_labels(self):
        c = self.canvas
        for (font, size), label in Labels.items():
            for x, y, align, color, text in label:
                w = c.stringWidth(text, fontName=font, fontSize=size)
                self.log("w = %f" % w)
                if x == -1:
                    x = self.width / 2
                if y == -1:
                    y = self.height / 2

                self.log("x = %f" % x)
                if align == 'CENTER':
                    x = x - (w / 2)
                t = c.beginText(x, self.height - y)
                t.setFont(font, size)
                t.setFillColor(color)
                t.textOut(text)
                c.drawText(t)

    def save(self, output):
        self.canvas.save()
        output.write(self.buff.getvalue())

    def log(self, msg):
        if self.verbose:
            print msg


def main():
    """This is the main stub, used for testing"""

    with open("test.pdf", "w+b") as f:
        form = BaseForm(verbose=1)
        form.save(f)


if __name__ == "__main__":
    import sys
    sys.exit(main())
