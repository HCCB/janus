#!/usr/bin/env python
from reportlab.lib.colors import black, red

inch = INCH = 72
cm = CM = inch / 2.54
Courier = 'Courier'
Helvetica = 'Helvetica'
Helvetica_Bold = 'Helvetica-Bold'
Helvetica_Oblique = 'Helvetica-Bold-Oblique'
OldEnglish = "OldEngMT"

FPOX = 0.05       # x offset for field positions
HX = 4.5 * inch   # x for centered text for letterhead

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

ly1 = (3.5 + 0.1) * cm
ly2 = (4 + 0.1) * cm
line_thin = [
    (0.8 * cm, 4.25 * cm, -0.8 * cm, 4.25 * cm, black),
    # Line for Name
    (2 * cm, ly1, 11 * cm, ly1, black),
    # Line for Date
    (12 * cm, ly1, 15.5 * cm, ly1, black),
    # Line for Case Number
    (17 * cm, ly1, 20 * cm, ly1, black),
    # line for Requesting Physician
    (4.45 * cm, ly2, 11 * cm, ly2, black),
    # line for Age
    (12 * cm, ly2, 13 * cm, ly2, black),
    # line for Sex
    (14 * cm, ly2, 15.5 * cm, ly2, black),
    # line for Room Number
    (17 * cm, ly2, 20 * cm, ly2, black),
]

Lines = {
    0.95: line_thick,
    0.25: line_thin,
}

# Text

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

    # master info labels
    (2 * cm, 3.5 * cm, 'RIGHT', black,
     'Name:'),
    (12 * cm, 3.5 * cm, 'RIGHT', black,
     'Date:'),
    (17 * cm, 3.5 * cm, 'RIGHT', black,
     'Case #:'),
    (4.45 * cm, 4 * cm, 'RIGHT', black,
     'Requesting Physician:'),
    (12 * cm, 4 * cm, 'RIGHT', black,
     'Age:'),
    (14 * cm, 4 * cm, 'RIGHT', black,
     'Sex:'),
    (17 * cm, 4 * cm, 'RIGHT', black,
     'Room#:'),
]

Labels = {
    (OldEnglish, 18): oldeng_18_text,
    (Helvetica_Bold, 10): helvetica_bold_9_text,
    (Helvetica, 10): helvetica_9_text,
}

TemplateData = {
    'Images': Images,
    'Lines': Lines,
    'Labels': Labels,
}
MASTER_FONT = Courier
MASTER_SIZE = 11
FP_MASTER_INFO = {
    'fullname': (
        ((2 + FPOX) * cm, 3.5 * cm),
        (MASTER_FONT, MASTER_SIZE, black),
    ),
    'date': (
        ((12 + FPOX) * cm, 3.5 * cm),
        (MASTER_FONT, MASTER_SIZE, black),
    ),
    'case_number': (
        ((17 + FPOX) * cm, 3.5 * cm),
        (MASTER_FONT, MASTER_SIZE, black),
    ),
    'physician': (
        ((4.45 + FPOX) * cm, 4 * cm),
        (MASTER_FONT, MASTER_SIZE, black),
    ),
    'age': (
        ((12 + FPOX) * cm, 4 * cm),
        (MASTER_FONT, MASTER_SIZE, black),
    ),
    'sex': (
        ((14 + FPOX) * cm, 4 * cm),
        (MASTER_FONT, MASTER_SIZE, black),
    ),
    'room_number': (
        ((17 + FPOX) * cm, 4 * cm),
        (MASTER_FONT, MASTER_SIZE, black),
    ),
}

testData = {
    'fullname': 'XXXXXXXXXX, XXXXXXXXXXXXXXXXX g.',
    'date': 'XX/XX/XX',
    'case_number': 'XXXXXXXXXX',
    'physician': 'DR. XXXXXXXXXXXXXXXXXXXX',
    'age': 'XX',
    'sex': 'XXXXXX',
    'room_number': 'XXXXXX',
}


def main():
    """Test stub for this file"""
    print black
    return 0

if __name__ == "__main__":
    import sys
    sys.exit(main())
