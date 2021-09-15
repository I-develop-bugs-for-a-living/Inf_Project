import pygame
import random

pic_monster = pygame.image.load("Enemys/alien.png")
pic_ufo = pygame.image.load("Enemys/enemy.png")
pic_ufo_eye = pygame.image.load("Enemys/ufu.png")


class Enemy:
    def __init__(self, win,  width, height):
        self.x = random.randint(100, 1100)
        self.y = random.randint(40, 200)
        self.width = width
        self.height = height
        self.imgs = [pic_monster, pic_ufo, pic_ufo_eye]
        self.health = [1, 2, 3]
        self.img = None
        self.win = win
        self.speed = random.choice([-8, -7, -6, -5, 5, 6, 7, 8])
        self.speed_y = 1
        self.color = (0, 0, 255)
        self.bullet_size = 32

    def draw(self):
        self.img = self.imgs[0]
        self.win.blit(self.img, (self.x, self.y))
        pygame.draw.line(self.win, self.color,
                         (self.x, self.y + self.height), (self.x + self.width, self.y + self.height), 4)
        self.move()

    def collide(self, bullet_x, bullet_y):
        if bullet_x > self.x and bullet_x < self.x + self.width:
            if bullet_y < self.y and bullet_y > self.y - self.height:
                return True
        elif bullet_x + self.bullet_size > self.x and bullet_x + self.bullet_size < self.x + self.width:
            if bullet_y < self.y and bullet_y > self.y - self.height:
                return True 
        else:
            return False

    def move(self):
        if self.x >= 1200 or self.x <= 0:
            self.speed *= -1
            self.y += 32
        self.x += self.speed
        self.y += self.speed_y
