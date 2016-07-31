from reportlab.lib.colors import black
from reportlab.lib.enums import TA_CENTER
from common import cm, Helvetica, Thin_Line

HEIGHT = 3.5
INTERVAL = 0.35
LINE1_Y = 0.5 * cm
LINE2_Y = HEIGHT * cm
LINE_Y = (HEIGHT - (INTERVAL * 3)) * cm
DrawData = {
    'Images': [],
    'Lines': {
        Thin_Line: [
            (0, LINE1_Y, 6 * cm, LINE1_Y, black),
            (0, LINE_Y, 6 * cm, LINE_Y, black),
            (0, LINE2_Y, 6 * cm, LINE2_Y, black),
        ],
    },
    'Labels': {},
}

FONTFACE = Helvetica
FONTSIZE = 10
XYPositions_1 = {
    'sig_name_1': (
        (3 * cm, (HEIGHT - (INTERVAL * 3) - 0.1) * cm),
        (FONTFACE, FONTSIZE, black),
        TA_CENTER,
        ),
    'sig_position_1': (
        (3 * cm, (HEIGHT - (INTERVAL * 2)) * cm),
        (FONTFACE, FONTSIZE, black),
        TA_CENTER,
        ),
    'sig_license_1': (
        (3 * cm,  (HEIGHT - (INTERVAL * 1)) * cm),
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
