import pygame

class Laser:
    def __init__(self, x, y, win):
        self.win = win
        self.x = x
        self.y = y

    def draw(self):
        pygame.draw.line(self.win, (self.x, self.y), (self.x, 0), 4)
