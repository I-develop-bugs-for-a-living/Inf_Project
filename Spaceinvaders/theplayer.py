import pygame
from bullet import Bullet

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, win, win_width, win_height):
        pygame.sprite.Sprite.__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.win = win
        self.win_width = win_width
        self.win_height = win_height
        # bullet
        self.cooldown_space = False
        self.cooldown_time_space = 20
        self.cooldown_timer_space = 0
        self.bullet_img = pygame.image.load("Bullets/laser one.png")
        # laser
        self.cooldown_q = False
        self.cooldown_time_q = 90
        self.cooldown_timer_q = 0
        self.onescreentime = 10
        # player
        self.img = pygame.image.load("Spaceship/Spaceship1.png")
        self.health = 5
        self.change_x = 0
        self.change_y = 0
        # development tools
        self.color = (255, 0, 0)
        self.bullets = []
        # sounds
        self.sound_shoot = pygame.mixer.Sound("Soundeff/laser_normal.wav")
        self.sound_flight = pygame.mixer.Sound("Soundeff/laser_normal.wav")

    def draw(self, pl_c_xr, pl_c_xl, pl_c_yu, pl_c_yd):
        self.win.blit(self.img, (self.x, self.y))
        self.move(pl_c_xr, pl_c_xl, pl_c_yu, pl_c_yd)
        for n, i in enumerate(self.bullets):
            i.draw()
            if i.y <= 0:
                self.bullets.pop(n)
                del i
        self.check_cooldown()
        self.draw_cooldown()

    def move(self, c_xr, c_xl, c_yu, c_yd):
        self.change_x = c_xr + c_xl
        self.change_y = c_yu + c_yd
        self.x += self.change_x
        self.y += self.change_y
        if self.y <= 10:
            self.y = 10
        if self.y >= self.win_height - 50:
            self.y = self.win_height - 50
        if self.x <= 10:
            self.x = 10
        if self.x >= self.win_width - 50:
            self.x = self.win_width - 50

    # shoot and cooldownsection start 
    def shoot(self):
        self.bullets.append(Bullet(self.x, self.y, self.win))
        self.sound_shoot.play()

    def shoot_q(self):
        pass

    def check_cooldown(self):
        if self.cooldown_space == True:    
            if self.cooldown_timer_space == self.cooldown_time_space:
                self.cooldown_space = False
                self.cooldown_timer_space = 0
            else:
                self.cooldown_timer_space += 1

    def draw_cooldown(self):
        if self.cooldown_space == False:
            pygame.draw.rect(self.win, (255, 255, 255), (30, self.win_height - 70, 40, 40))
        else:
            pygame.draw.rect(self.win, (255, 255, 255), (30, self.win_height - 30 - self.cooldown_timer_space * 2, 40, 40))
        pygame.draw.circle(self.win, (255, 0, 0), (50, self.win_height - 50), 20, 2)
        pygame.draw.circle(self.win, (255, 255, 0), (50, self.win_height - 50), 70, 50)
        self.win.blit(self.bullet_img, (34, self.win_height - 62))
    # shoot and cooldownsection end

    def hit(self):
        pass

    def collide(self):
        pygame.draw.line(self.win, self.color, (self.x, self.y), (self.x + 32, self.y), 4)