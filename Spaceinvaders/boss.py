import pygame
import random

class Boss:
    def __init__(self, win, height, width, lvl=1):
        self.height = height
        self.width = width
        self.x = random.randint(300, 900)
        self.y = random.randint(20, 200)
        self.win = win
        self.lvl = lvl
        self.img = pygame.image.load("Enemys/enemy.png")
        self.speed = random.randint(-10, 10)
        # testing
        self.color = (0, 255, 0)

    def draw(self):
        self.win.blit(self.img, (self.x, self.y))
        self.move()

    def move(self):
        self.x += self.speed
        if self.x >= 1000 or self.x <= 200:
            self.speed *= -1
            self.shoot()

    def collide(self, bullet_x, bullet_y):
        pygame.draw.line(self.win, self.color,
                         (self.x, self.y + self.height), (self.x + self.width, self.y + self.height), 4)

    def shoot(self):
        pass