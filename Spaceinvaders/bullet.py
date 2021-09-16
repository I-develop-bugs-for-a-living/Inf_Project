import pygame 

class Bullet:
    def __init__(self, x, y, win):
        # inheritate
        self.win = win
        # bulletdetails
        self.x = x
        self.y = y
        self.img = pygame.image.load("Bullets/laser one.png") 
        self.cooldown_space = 10
        self.speed = -30
        self.damage = 1

    def draw(self):
        self.win.blit(self.img, (self.x, self.y))
        self.move()

    def move(self):
        self.y += self.speed
        

            
        