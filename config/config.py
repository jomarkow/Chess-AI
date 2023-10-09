import numpy as np

# ------ BOARD -------

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
DISTANCE = SIZE * 2
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

BLACK_YELLOW = "../data/images/boards/yellow_black_up.jpeg"