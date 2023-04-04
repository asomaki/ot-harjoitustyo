import pygame
import os
dirname = os.path.dirname(__file__)

class Peli2048:
    def __init__(self):
        pygame.init()
        self.load_pictures()
        self.new_game()
        self.height = len(self.map)
        self.width = len(self.map[0])
        self.square_size = 50

        self.display = pygame.display.set_mode((200, 200))

        pygame.display.set_caption("2048")

        self.loop()

    def load_pictures(self):
        self.pictures = []
        
        self.pictures.append(pygame.image.load(os.path.join(dirname, "assets", "floor.png")))

    def new_game(self):
        self.map = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

    def loop(self):
        while True:
            self.events()
            self.draw_display()
    
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
    
    def draw_display(self):
        self.display.fill((0, 0, 0))

        for y in range(4):
            for x in range(4):
                square = self.map[y][x]
                norm_x = x * self.square_size
                norm_y = y * self.square_size
                self.display.blit(self.pictures[square], (norm_x, norm_y))

        pygame.display.flip()

if __name__ == "__main__":
    Peli2048()