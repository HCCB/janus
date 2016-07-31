from reportlab.lib.colors import black
from reportlab.lib.enums import TA_CENTER
from common import cm, Helvetica, Thin_Line

FONTFACE = Helvetica
FONTSIZE = 8

HEIGHT = 1.2
WIDTH = 6.5
MID = (WIDTH / 2) * cm
INTERVAL = 0.30

LINE1_Y = 0
LINE2_Y = HEIGHT * cm
LINE_Y = (HEIGHT - (INTERVAL * 3)) * cm

DrawData = {
    'Images': [],
    'Lines': {
        Thin_Line: [
            (0, LINE_Y, WIDTH * cm, LINE_Y, black),
            # (0, LINE1_Y, WIDTH * cm, LINE1_Y, black),  # top line
            # (0, LINE2_Y, WIDTH * cm, LINE2_Y, black),  # bottom line
            # (MID, 0, MID, HEIGHT * cm, black),  # show middle
        ],
    },
    'Labels': {},
}

XYPositions_1 = {
    'sig_name_1': (
        (MID, (HEIGHT - (INTERVAL * 3) - 0.1) * cm),
        (FONTFACE, FONTSIZE, black),
        TA_CENTER,
        ),
    'sig_position_1': (
        (MID, (HEIGHT - (INTERVAL * 2)) * cm),
        (FONTFACE, FONTSIZE, black),
        TA_CENTER,
        ),
    'sig_license_1': (
        (MID,  (HEIGHT - (INTERVAL * 1)) * cm),
        (FONTFACE, FONTSIZE, black),
        TA_CENTER,
        ),
    }

SignatureForm1 = (DrawData, XYPositions_1)

sigformtest1 = {
    'sig_name_1': 'XXXXXXXXX X. XXXXXXXXX, XXX',
    'sig_position_1': 'XXXXXXXXXXXXXXX',
    'sig_license_1': 'LIC NO. XXXXXXXXXX',
}
XYPositions_2 = {
    'sig_name_2': (
        (MID, (HEIGHT - (INTERVAL * 3) - 0.1) * cm),
        (FONTFACE, FONTSIZE, black),
        TA_CENTER,
        ),
    'sig_position_2': (
        (MID, (HEIGHT - (INTERVAL * 2)) * cm),
        (FONTFACE, FONTSIZE, black),
        TA_CENTER,
        ),
    'sig_license_2': (
        (MID,  (HEIGHT - (INTERVAL * 1)) * cm),
        (FONTFACE, FONTSIZE, black),
        TA_CENTER,
        ),
    }

SignatureForm2 = (DrawData, XYPositions_2)

sigformtest2 = {
    'sig_name_2': '22XXXXXXXXX X. XXXXXXXXX, XXX',
    'sig_position_2': '22XXXXXXXXXXXXXXX',
    'sig_license_2': 'LIC NO. 2222222222',
}
