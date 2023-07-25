from game_config import *
import pygame
import chess
import sys

board = [
    ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
    ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
    ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
]

names = {"B":"black_bishop","K":"black_king","N":"black_knight","P":"black_pawn","Q":"black_queen","R":"black_rook", 
        "b":"white_bishop","k":"white_king","n":"white_knight","p":"white_pawn","q":"white_queen","r":"white_rook",}


screen = init_game()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Clear the screen
    screen.fill(WHITE)
    
    

    # Draw the chessboard
    
    pygame.draw.line(screen, BLACK, (MARGIN, MARGIN), (WIDTH, MARGIN), 5)
    pygame.draw.line(screen, BLACK, (MARGIN, MARGIN), (MARGIN, HEIGHT), 5)
    
    for row in range(8):
        for col in range(8):
            
            grid_to_px = col * SQUARE_SIZE + MARGIN, row * SQUARE_SIZE + MARGIN
            
            color = WHITE if (row + col) % 2 == 0 else GREEN
            
            pygame.draw.rect(screen, color, (*grid_to_px, SQUARE_SIZE, SQUARE_SIZE))
            
            if board[row][col] != ".":
                image_name = names[board[row][col]]
                image = pygame.image.load(f"images\{image_name}.png")
                screen.blit(image, grid_to_px)
            

    # Update the display
    pygame.display.flip()
