import pygame
from pygame.locals import *
import os
import sys
import math

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGTH = int(SCREEN_WIDTH * 0.8)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGTH))
pygame.display.set_caption('Aadoaaljs fdjlhkfdsa')


# defining player action variables
moving_left = False
moving_right = False

class Soldier(pygame.sprite.Sprite):
    def __init__(self, x, y, scale, speed) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.speed = speed
        img = pygame.image.load('assets/player/alien.png')
        self.image = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
    
    def draw(self):
        screen.blit(self.image, self.rect)

player = Soldier(200, 200, 3, 10)

run = True
while run:


    player.draw()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                moving_left = True
            if event.key == pygame.K_d:
                moving_right = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                moving_left = False
            if event.key == pygame.K_d:
                moving_right = False
            if event.key == pygame.K_ESCAPE:
                run = False
    pygame.display.update()

pygame.quit()