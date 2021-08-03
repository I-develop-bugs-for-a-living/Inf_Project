import pygame
from pygame.locals import *
import os
import sys
import math

pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGTH = int(SCREEN_WIDTH * 0.7)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGTH))
pygame.display.set_caption('Tolles Spiel')

# set framerate
clock = pygame.time.Clock()
FPS = 60

# define Colors
BG = (144, 201, 120)

# defining player action variables
moving_left = False
moving_right = False

def draw_bg():
    screen.fill(BG)

class Soldier(pygame.sprite.Sprite):
    def __init__(self, char_type, x, y, scale, speed) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.char_type = char_type
        self.speed = speed
        self.direction = 1
        self.flip = True
        self.animation_list = []
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
        for i in range(5):
            img = pygame.image.load(f'assets/{char_type}/Idle/{i}.png')
            img = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
            self.animation_list.append(img)
        self.image = self.animation_list[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
    
    def move(self, moving_left, moving_right):
        dx = 0
        dy = 0
        if moving_right:
            dx = self.speed
            self.flip = False
            self.direction = -1
        if moving_left:
            dx = -self.speed
            self.flip = True
            self.direction = 1

        self.rect.x += dx
        self.rect.y += dy

    def update_animation(self):
        # update animation
        ANIMATION_COOLDOWN = 100
        # update image 
        self.image = self.animation_list[self.frame_index]
        # check time past
        if pygame.time.get_ticks() - self.update_time > ANIMATION_COOLDOWN:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        if self.frame_index >= len(self.animation_list):
            self.frame_index = 0

    def draw(self):

        screen.blit(pygame.transform.flip(self.image, self.flip, False),self.rect)

player = Soldier('player', 200, 200, 3, 5)

run = True
while run:
    clock.tick(FPS)
    draw_bg()
    player.update_animation()
    player.draw()
    player.move(moving_left, moving_right)


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