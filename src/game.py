import pygame

from board import Board
from const import *

class Game:
    def __init__(self):
        self.board = Board()
    
    #show methods

    #background color design
    def show_bg(self, surface):
        for row in range(ROWS):
            for col in range(COLUMNS):
                if (row + col) % 2 == 0:
                    color = (0, 238, 238)
                    #color = (234, 235, 200) #light green
                else:
                    color = (0, 139, 139)
                    #color = (119, 154, 88) #dark green
                
                rectangle = (col * SQSIZE, row * SQSIZE, SQSIZE, SQSIZE)

                pygame.draw.rect(surface, color, rectangle)

    def show_pieces(self, surface):
        for row in range(ROWS):
            for col in range(COLUMNS):
                #check if there is a piece on the square
                if self.board.squares[row][col].has_piece():
                    piece = self.board.squares[row][col].piece

                    img = pygame.image.load(piece.texture)
                    img_center = col * SQSIZE + SQSIZE //2, row * SQSIZE + SQSIZE //2
                    piece.texture_rect = img.get_rect(center = img_center)
                    surface.blit(img, piece.texture_rect)
