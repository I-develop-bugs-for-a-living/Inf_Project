import pygame

class player(object):

    def __init__(self, x, y, width, heigth):
        self.x = x
        self.y = y
        self.width = width
        self.heigth = heigth
        self.jumping = False
        self.jumpCount = 0

    def draw(self, win):
        win.blit()