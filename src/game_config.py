import pygame
#screen

SQUARE_SIZE = 80
MARGIN = 40
WIDTH = SQUARE_SIZE * 8 + MARGIN
HEIGHT = WIDTH

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 100, 0)

def init_game():
    
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Chess")
    
    return screen