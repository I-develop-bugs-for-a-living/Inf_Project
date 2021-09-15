import pygame
# import os
from enemy import Enemy
from theplayer import Player
from boss import Boss
import random


class Game:
    def __init__(self, num_enemies, width, height, boss_state=False, fps=30):
        # win
        self.width = width
        self.height = height
        self.win = pygame.display.set_mode((self.width, self.height))
        self.bg = pygame.image.load("Bg/background.png")
        self.fps = fps
        # player and enemies            
        self.player = Player(400, 400, 32, 32, self.win, self.width, self.height)
        self.num_enemies = num_enemies
        self.boss_state = boss_state
        self.enemies = []
        self.state_collision = []
        # score
        self.font = pygame.font.Font("freesansbold.ttf", 25)
        self.score = 0
        self.score_object = ""
        self.score_x = 10
        self.score_y = 10 

    def set_up(self):
        for _ in range(self.num_enemies):
            self.enemies.append(Enemy(self.win, 32, 32))
        if self.boss_state:
            self.enemies.append(Boss(self.win, 32, 32))

    def run(self):
        run = True
        clock = pygame.time.Clock()
        pl_c_yu = 0
        pl_c_xr = 0
        pl_c_xl = 0
        pl_c_yd = 0
        while run:
            # fps
            clock.tick(self.fps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_ESCAPE:
                        run = False

                    if event.key == pygame.K_UP:
                        pl_c_yu = -15

                    if event.key == pygame.K_DOWN:
                        pl_c_yd = 15

                    if event.key == pygame.K_LEFT:
                        pl_c_xl = -15

                    if event.key == pygame.K_RIGHT:
                        pl_c_xr = 15

                    if event.key == pygame.K_SPACE:
                        if not self.player.cooldown_space:
                            self.player.shoot()
                            self.player.cooldown_space = True
                    
                    if event.key == pygame.K_q:
                        if not self.player.cooldown_q:
                            self.player.shoot_q()
                            self.player.cooldown_q = True

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        pl_c_xl = 0

                    if event.key == pygame.K_RIGHT:
                        pl_c_xr = 0

                    if event.key == pygame.K_UP:
                        pl_c_yu = 0

                    if event.key == pygame.K_DOWN:
                        pl_c_yd = 0

            # the player_change_rates in a list to make the function_call shorter
            pl_c = [pl_c_xr, pl_c_xl, pl_c_yu, pl_c_yd]
            self.draw(pl_c)

        pygame.quit()

    def draw(self, pl_c):
        self.win.blit(self.bg, (0, 0))
        # containing the change in a list
        self.player.collide()
        self.player.draw(pl_c[0], pl_c[1], pl_c[2], pl_c[3])
        self.collide()
        self.score_draw()
        pygame.display.update()

    def score_draw(self):
        self.score_object = self.font.render("Score: " + str(self.score), True, (0, 255, 0))
        self.win.blit(self.score_object, (self.score_x, self.score_y))

    def collide(self):
        for i in self.enemies:
            if len(self.player.bullets) > 0:
                for n, j in enumerate(self.player.bullets):
                    if i.collide(j.x, j.y):
                        del j
                        self.player.bullets.pop(n)
                        i.x = random.randint(100, 1100)
                        i.y = random.randint(40, 400)
                        self.score += 1
            i.draw()
            if i.y >= self.height:
                self.score -= 20
                i.x = random.randint(100, 1100)
                i.y = random.randint(40, 400)
