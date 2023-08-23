from game_config import *
import pandas as pd
import pygame
import chess
import sys


names = {"B":"black_bishop","K":"black_king","N":"black_knight","P":"black_pawn","Q":"black_queen","R":"black_rook", 
        "b":"white_bishop","k":"white_king","n":"white_knight","p":"white_pawn","q":"white_queen","r":"white_rook",}

board_list = [
    ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
    ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
    ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
]
 
board = pd.DataFrame(board_list,columns=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'])
board.index = [8,7,6,5,4,3,2,1]

screen = init_game()

def move(coor, board = board):


    piece = coor[0]
    from_col = coor[1]
    from_row = int(coor[2])
    to_col = coor[4]
    to_row = int(coor[5])

    if(board[from_col][from_row] != piece):

        print("Piece not in position")
    else:
        board[to_col][to_row] = piece
        board[from_col][from_row] = "."
        

def run_game(board = board):
    board = board.values
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
                    image = pygame.image.load(f"images\pieces\{image_name}.png")
                    screen.blit(image, grid_to_px)
                

        # Update the display
        pygame.display.flip()
