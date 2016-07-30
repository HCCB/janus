from reportlab.lib.colors import black
from data_common import *

ly1 = (3.5 + 0.1) * cm
ly2 = (4 + 0.1) * cm
line_normal = [
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
    # bottom line
    (0.8 * cm, 4.25 * cm, -0.8 * cm, 4.25 * cm, black),
    ]
Lines = {
    0.25: line_normal,
    }

text_normal = [
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
    (Helvetica, 10): text_normal,
    }
    
MasterData = {
    'Images': [],
    'Lines': Lines,
    'Labels': Labels
    }
    

FPOX = 0.05       # x offset for field positions
MASTER_FONT = Courier
MASTER_SIZE = 11
XYPositions = {
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

MasterForm = (MasterData, XYPositions)

testData = {
    'fullname': 'XXXXXXXXXX, XXXXXXXXXXXXXXXXX g.',
    'date': 'XX/XX/XX',
    'case_number': 'XXXXXXXXXX',
    'physician': 'DR. XXXXXXXXXXXXXXXXXXXX',
    'age': 'XX',
    'sex': 'XXXXXX',
    'room_number': 'XXXXXX',
}
