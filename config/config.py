import numpy as np

# ------ BOARD -------

class Board:
    SQUARE_SIZE = 80
    MARGIN = 40
    WIDTH = SQUARE_SIZE * 8 + MARGIN
    HEIGHT = WIDTH
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GREEN = (0, 100, 0)

# -------- GRID RECOG -----------

# Board
SIZE = 700
DISTANCE = 2 * SIZE
VERTICAL = 0
HORIZONTAL = 1
EDGES = 3

# Filters
THRESHOLD1 = 90
THRESHOLD2 = 400
HOUGH_THRESHOLD = 100
THETA_RESOLUTION = np.pi / 180
RHO_RESOLUTION = 1

# Debug color
RED = (0, 0, 255)
BLUE = (255, 0, 0)
GREEN = (0, 255, 0)

# Corners
MAX_CORNERS = 81
QUALITY = .5
MIN_DISTANCE = 30

# Images path

BLACK_YELLOW_UP = "../data/images/boards/yellow_black_up.jpeg"
BLACK_WHITE_UP = "../data/images/boards/black_white_up.jpeg"
RED_WHITE_UP = "../data/images/boards/red_white_up.jpeg"
RED_WHITE_ANGLED = "../data/images/boards/red_white_angled.jpeg"
RED_WHITE_ANGLED_ROMBO = "../data/images/boards/red_white_angled_rombo.jpeg"
# ---------- CONNECTIVITY -----------

ADDRESS = "Smart_chess"
PORT = 1883