import pygame
import sys 
from const import * #screen dimension and board dimension
from game import Game

class Main:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT)) #black screen
        pygame.display.set_caption("Chess")
        self.game = Game() #reference
    
    def mainloop(self):
        #setup pygame file; always the same for main loop
        screen = self.screen
        game = self.game

        while True:
            self.game.show_bg(screen)
            self.game.show_pieces(screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    # loop through each event in pygame

            #render background; chess game displayed on screen
            
            pygame.display.update()

main = Main()
main.mainloop()


