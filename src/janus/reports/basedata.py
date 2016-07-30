#!/usr/bin/env python
from reportlab.lib.colors import black, red

inch = INCH = 72
cm = CM = inch / 2.54
Courier = 'Courier'
Helvetica = 'Helvetica'
Helvetica_Bold = 'Helvetica-Bold'
Helvetica_Oblique = 'Helvetica-Bold-Oblique'

OldEnglish = "OldEngMT"

# Images
Images = [
    (
        './static/HCCB-Hospital-Logo.png',
        0.2 * cm,   # left
        0.2 * cm,   # top
        2.85 * cm,  # height
        'auto',     # mask
        True,       # preserveAspectRatio
    ),
]

# Lines 
line_thick = [
    (0.5 * cm, 3.05 * cm, -0.5 * cm, 3.05 * cm, red),
]
line_thin = [
    (0.8 * cm, 5.25 * cm, -0.8 * cm, 5.25 * cm, black),
]

Lines = {
    0.95: line_thick,
    0.25: line_thin,
}

# Text

HX = 4.5 * inch

oldeng_18_text = [
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
    (OldEnglish, 18): oldeng_18_text,
    (Helvetica_Bold, 9): helvetica_bold_9_text,
    (Helvetica, 9): helvetica_9_text,
}

TemplateData = {
    'Images': Images,
    'Lines': Lines,
    'Labels': Labels,
}


def main():
    """Test stub for this file"""

    return 0

if __name__ == "__main__":
    import sys
    sys.exit(main())
