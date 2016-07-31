#!/usr/bin/env python
from io import BytesIO

from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import A5, landscape
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab .lib.enums import TA_CENTER, TA_RIGHT
from reportlab.lib.units import cm

from data.common import Courier

# load fonts
import os.path
basedir = os.path.dirname(os.path.realpath(__file__))
ttfFile = os.path.join(basedir, 'fonts/oldeng.ttf')
pdfmetrics.registerFont(TTFont("OldEngMT", ttfFile))


class BaseForm(object):
    def __init__(self, **kw):
        super(BaseForm, self).__init__()

        self.positions = {}

        self.buff = BytesIO()
        self.verbose = kw.get('verbose', 0)
        self.fontface = kw.get('fontface', Courier)
        self.fontsize = kw.get('fontsize', 10)

        self.log("creating canvas")
        self.canvas = Canvas(self.buff)
        pagesize = kw.get("pagesize", landscape(A5))
        self.width, self.height = pagesize

        self.log("pagesize = %s" % str(pagesize))
        self.canvas.setPageSize(pagesize)

    def draw_template(self, template_data, **kw):
        func_mapping = {
            'Images': self.__draw_images,
            'Labels': self.__draw_text_labels,
            'Lines': self.__draw_lines,
            }

        ofsx = kw.get("ofsx", 0)
        ofsy = kw.get("ofsy", 0)

        for k, data in template_data.items():
            func_mapping[k](data, ofsx, ofsy)

    def __draw_images(self, data, ofsx, ofsy):
        for img, x, y, h, mask, aspect in data:
            x += ofsx
            y += ofsy
            img_path = os.path.join(basedir, img)
            self.log("opening image - %s" % img_path)
            self.canvas.drawImage(img_path, x, self.height - h - y,
                                  height=h,
                                  mask=mask, preserveAspectRatio=aspect)

    def __draw_text_labels(self, data, ofsx, ofsy):
        c = self.canvas
        for (font, size), label in data.items():
            for x, y, align, color, text in label:
                w = c.stringWidth(text, fontName=font, fontSize=size)
                if x == -1:
                    x = self.width / 2
                if y == -1:
                    y = self.height / 2

                if align == 'CENTER':
                    x = x - (w / 2)
                elif align == 'RIGHT':
                    x = x - w
                x += ofsx
                y += ofsy
                t = c.beginText(x, self.height - y)
                t.setFont(font, size)
                t.setFillColor(color)
                t.textOut(text)
                c.drawText(t)

    def __draw_lines(self, data, ofsx, ofsy):
        c = self.canvas
        for width, lines in data.items():
            for x1, y1, x2, y2, color in lines:
                if x2 < 0:
                    x2 = self.width + x2
                if y2 < 0:
                    y2 = abs(y2)
                else:
                    y2 = self.height - y2
                if y1 < 0:
                    y1 = abs(y1)
                else:
                    y1 = self.height - y1

                x1 += ofsx
                x2 += ofsx
                y1 -= ofsy
                y2 -= ofsy
                c.setStrokeColor(color)
                c.setLineWidth(width)
                c.line(x1, y1, x2, y2)

    def save(self, output):
        self.canvas.save()
        output.write(self.buff.getvalue())

    def log(self, msg):
        if self.verbose:
            print msg

    def add_form(self, formdata, **kw):
        from copy import deepcopy
        template, xypositions = formdata
        ofsx = kw.get('ofsx', 0)
        ofsy = kw.get('ofsy', 0)
        positions = deepcopy(xypositions)
        if ofsx or ofsy:
            # we will update the xy positions adding the corresponding offset
            for k, v in positions.items():
                coord, other, align = v
                x, y = coord
                positions[k] = ((x+ofsx, y+ofsy), other, align)

        self.positions.update(positions)
        self.draw_template(template, **kw)

    def populate(self, dict, **kw):
        c = self.canvas
        ofsx = kw.get("ofsx", 0)
        ofsy = kw.get("ofsy", 0)
        positions = self.positions
        for k, v in dict.items():
            if k not in positions:
                if self.verbose:
                    print "populate() item not found - %s" % k
                continue
            (x, y), (fontface, fontsize, color), align = positions[k]
            y = (self.height - y) - ofsy
            x = x + ofsx
            w = c.stringWidth(v, fontName=fontface, fontSize=fontsize)
            if align == TA_CENTER:
                x = x - (w / 2)
            elif align == TA_RIGHT:
                x = x - w
            t = c.beginText(x, y)
            t.setFont(fontface, fontsize)
            t.setFillColor(color)
            t.textOut(v)
            c.drawText(t)


class FormElectrolytes(BaseForm):
    def __init__(self, **kw):
        from data.master import MasterForm
        super(FormElectrolytes, self).__init__(**kw)
        self.__draw_header()
        self.add_form(MasterForm)

    def __draw_header(self):
        from data.header import HeaderData
        self.draw_template(HeaderData)


def main():
    """This is the main stub, used for testing"""
    from data.master import testData, XYPositions
    from data.signatory import SignatureForm1, sigformtest1
    from data.signatory import SignatureForm2, sigformtest2
    from pickle import dumps, loads

    data = dumps(XYPositions)
    obj = loads(data)

    print data
    print obj

    with open("test.pdf", "w+b") as f:
        # form = BaseForm(verbose=1, templatedata=TemplateData)
        form = FormElectrolytes(verbose=1)
        form.add_form(SignatureForm1, ofsy=13*cm, ofsx=20)
        form.add_form(SignatureForm2, ofsy=13*cm, ofsx=400)
        form.populate(sigformtest1)
        form.populate(sigformtest2)
        form.populate(testData)
        form.save(f)


if __name__ == "__main__":
    import sys
    sys.exit(main())
