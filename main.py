import pygame
import chess.svg as imgs
import chess

board = chess.Board()

# Initialize Pygame
pygame.init()

# Set up the screen
WIDTH, HEIGHT = 400, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Size of each square
SQUARE_SIZE = WIDTH // 8

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            #Hola como estas
            sys.exit()

    # Clear the screen
    screen.fill(WHITE)

    # Draw the chessboard
    for row in range(8):
        for col in range(8):
            color = WHITE if (row + col) % 2 == 0 else BLACK
            pygame.draw.rect(screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    # Update the display
    pygame.display.flip()
