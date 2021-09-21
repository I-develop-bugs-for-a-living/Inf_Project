import pygame
from pygame.locals import *
import os
import sys
import math
pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGTH = int(SCREEN_WIDTH * 0.7)

TILE_SIZE = 40

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGTH))
pygame.display.set_caption('Tolles Spiel')

# set framerate
clock = pygame.time.Clock()
FPS = 60

# game variables
GRAVITY = 0.75

# define Colors
BG = (144, 201, 120)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# load images
# bullet
bullet_img = pygame.transform.rotate(pygame.image.load('assets/game/icons/bullet.png').convert_alpha(), 90)
# grenade
grenade_img = pygame.transform.scale(pygame.image.load('assets/game/Pixilart Sprite Sheet.jpg').convert_alpha(), (20, 20))
# bg
bg_img = pygame.transform.scale(pygame.image.load('assets/bg/bg.png'), (1000, 720))
# boxes
health_box_img = pygame.image.load('assets/game/icons/health_box.png').convert_alpha()
ammo_box_img = pygame.image.load('assets/game/icons/ammo_box.png').convert_alpha()
grenade_box_img = pygame.image.load('assets/game/icons/grenade_box.png').convert_alpha()
speed_box_img = pygame.image.load('assets/game/icons/grenade_box.png').convert_alpha()
jump_box_img = pygame.image.load('assets/game/icons/grenade_box.png').convert_alpha()
damage_box_img = pygame.image.load('assets/game/icons/grenade_box.png').convert_alpha()

item_boxes = {
    'Health' : health_box_img,
    'Ammo'  : ammo_box_img,
    'Grenade' : grenade_box_img,
    'Speed' : speed_box_img,
    'Jump'  : jump_box_img,
    'Damage' : damage_box_img,
}
# defining player action variables
moving_left = False
moving_right = False
shoot = False
grenade = False
grenade_thrown = False

#font
font = pygame.font.SysFont('Futura', 30)

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

# draw background color
def draw_bg():
    screen.blit(bg_img, (0,0))
    pygame.draw.line(screen, RED, (0, 300), (SCREEN_WIDTH, 300))

class ItemBox(pygame.sprite.Sprite):
    def __init__(self, item_type, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.item_type = item_type
        self.image = item_boxes[self.item_type]
        self.rect = self.image.get_rect()
        self.rect.midtop = (x + TILE_SIZE // 2, y + (TILE_SIZE - self.image.get_height()))

    def update(self):
        if pygame.sprite.collide_rect(self, player):
            if self.item_type == 'Health':
                player.health += 25
                if player.health > player.max_health:
                    player.health = player.max_health
            elif self.item_type == 'Ammo':
                player.ammo += 15
            elif self.item_type == 'Grenade':
                player.grenades += 3
            elif self.item_type == 'Speed':
                player.speed += 5
            elif self.item_type == 'Jump':
                player.jump_heigth -= 4
            elif self.item_type == 'Damage':
                player.health -= 5
                player.speed -= 5
            self.kill()

class Grenade(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        pygame.sprite.Sprite.__init__(self)
        self.timer = 100
        self.vel_y = -11
        self.speed = 7
        self.image = grenade_img
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.direction = direction

    def update(self):
        self.vel_y += GRAVITY
        dx = self.direction * self.speed
        dy = self.vel_y
        
        # don't go through the floor
        if self.rect.bottom + dy > 300:
            dy = 300 - self.rect.bottom
            self.speed = 0

        # don't go through the wall
        if self.rect.left + dx < 0 or self.rect.right + dx > SCREEN_WIDTH:
            self.direction *= -1
            dx = self.direction * self.speed

        # update grenade position
        self.rect.x += dx
        self.rect.y += dy

        # countdown timer
        self.timer -= 1
        if self.timer <= 0:
            self.kill()
            explosion = Explosion(self.rect.x, self.rect.y, 0.5)
            explosion_group.add(explosion)

            # do damage
            if abs(self.rect.centerx - player.rect.centerx) < TILE_SIZE * 2 and abs(self.rect.centery - player.rect.centery) < TILE_SIZE * 2:
                player.health -= 50
            for enemy in enemy_group:
                if abs(self.rect.centerx - enemy.rect.centerx) < TILE_SIZE * 2 and abs(self.rect.centery - enemy.rect.centery) < TILE_SIZE * 2:
                    enemy.health -= 50
        
class Explosion(pygame.sprite.Sprite):
    def __init__(self, x, y, scale):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        for num in range(1, 6):
            img = pygame.image.load(f'assets/game/explosion/exp{num}.png').convert_alpha()
            img = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
            self.images.append(img)
        self.index = 0
        self.frame_index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.counter = 0

    def update(self):
        EXPLOSION_SPEED = 4
        self.counter += 1

        if self.counter >= EXPLOSION_SPEED:
            self.counter = 0
            self.frame_index += 1
            if self.frame_index >= len(self.images):
                self.kill()
            else:
                self.image = self.images[self.frame_index]
        
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 10
        self.image = bullet_img
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.direction = direction

    def update(self):
        # move bullet
        self.rect.x += (self.direction * self.speed)
        # check if bullet of screen
        if self.rect.right < 0 or self.rect.left > SCREEN_WIDTH:
            self.kill()
        
        # check collision with character
        if pygame.sprite.spritecollide(player, bullet_group, False):
            if player.alive:
                player.health -= 5
                self.kill()

        for enemy in enemy_group:
            if pygame.sprite.spritecollide(enemy, bullet_group, False):
                if enemy.alive:
                    enemy.health -= 100
                    self.kill()


class Soldier(pygame.sprite.Sprite):
    def __init__(self, char_type, x, y, scale, speed, ammo, grenades) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.alive = True
        self.char_type = char_type
        self.speed = speed
        self.ammo = ammo
        self.start_ammo = ammo
        self.shoot_cooldown = 0
        self.health = 100
        self.grenades = grenades
        self.max_health = self.health
        self.direction = 1
        self.vel_y = 0
        self.jump_heigth = -11
        self.jump = False
        self.in_air = True
        self.flip = True
        self.animation_list = []
        self.frame_index = 0
        self.action = 0
        self.update_time = pygame.time.get_ticks()

        # load all images for the players
        animation_types = ['Idle', 'Run', 'Jump', 'Death']
        for animation in animation_types:
            temp_list = []
            # count num of files in folder
            num_of_frames = len(os.listdir(f'assets/{self.char_type}/{animation}'))
            for i in range(num_of_frames):
                img = pygame.image.load(f'assets/{char_type}/{animation}/{i}.png').convert_alpha()
                img = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
                temp_list.append(img)
            self.animation_list.append(temp_list)
        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self):
        self.update_animation()
        self.check_alive()
        # update cooldown
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1
        
    
    def move(self, moving_left, moving_right):
        dx = 0
        dy = 0
        if moving_right:
            dx = self.speed
            self.flip = False
            self.direction = 1
        if moving_left:
            dx = -self.speed
            self.flip = True
            self.direction = -1

        # jump
        if self.jump == True and self.in_air == False:
            self.vel_y = self.jump_heigth
            self.jump = False
            self.in_air = True
        
        # apply gravity
        self.vel_y += GRAVITY
        if self.vel_y > 10:
            self.vel_y = 10
        dy += self.vel_y

        # check collision with floor
        if self.rect.bottom + dy > 300:
            dy = 300 - self.rect.bottom
            self.in_air = False

        self.rect.x += dx
        self.rect.y += dy

    def shoot(self):
        if self.shoot_cooldown == 0 and self.ammo > 0:
            self.shoot_cooldown = 20
            bullet = Bullet(player.rect.centerx + (0.7 * player.rect.size[0] * player.direction), player.rect.centery, player.direction)
            bullet_group.add(bullet)
            # subtract from ammo variable
            self.ammo -= 1

    def update_animation(self):
        # update animation
        ANIMATION_COOLDOWN = 100
        # update image 
        self.image = self.animation_list[self.action][self.frame_index]
        # check time past
        if pygame.time.get_ticks() - self.update_time > ANIMATION_COOLDOWN:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        if self.frame_index >= len(self.animation_list[self.action]):
            if self.action == 3:
                self.frame_index = len(self.animation_list[self.action]) - 1
            else:
                self.frame_index = 0
    
    def update_action(self, new_action):
        # check if action changed
        if new_action != self.action:
            self.action = new_action
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()

    def check_alive(self):
        if self.health <= 0:
            self.health = 0
            self.speed = 0
            self.alive = False
            self.update_action(3)

    def draw(self):

        screen.blit(pygame.transform.flip(self.image, self.flip, False),self.rect)


# create  sprite groups
enemy_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()
grenade_group = pygame.sprite.Group()
explosion_group = pygame.sprite.Group()
item_box_group = pygame.sprite.Group()

# temp - create item boxes
a = 200
for i in ["Ammo", "Health", "Grenade"]:
    item_box = ItemBox(i, a, 260)
    a += 100
    item_box_group.add(item_box)

player = Soldier('player', 200, 200, 3, 5, 20, 5)
enemy = Soldier('enemy', 200, 200, 3, 5, 20, 0)
enemy2 = Soldier('enemy', 300, 300, 3, 5, 20, 0)

enemy_group.add(enemy)
enemy_group.add(enemy2)

run = True
while run:
    clock.tick(FPS)

    draw_bg()

    # show ammo and grenades
    draw_text('AMMO: ', font, WHITE, 10, 35)
    for x in range(player.ammo):
        screen.blit(bullet_img, (90 + (x * 10), 35))
    # show grenades
    draw_text('GRENADE: ', font, WHITE, 10, 60)
    for x in range(player.grenades):
        screen.blit(grenade_img, (120 + (x * 15), 60))

    for enemy in enemy_group:
        enemy.update()
        enemy.draw()

    player.update()
    player.draw()


    # draw groups
    bullet_group.update()
    grenade_group.update()
    explosion_group.update()
    item_box_group.update()
    bullet_group.draw(screen)
    grenade_group.draw(screen)
    explosion_group.draw(screen)
    item_box_group.draw(screen)

    if player.alive:
        if shoot:
           player.shoot()
        # trigger grenade
        elif grenade and not grenade_thrown and player.grenades > 0:
            grenade_projectile = Grenade(player.rect.centerx + (0.5 * player.rect.size[0] * player.direction), player.rect.top, player.direction)
            grenade_group.add(grenade_projectile)
            player.grenades -= 1
            grenade_thrown = True
        
        if player.in_air:
            player.update_action(2)
        if moving_left or moving_right:
            player.update_action(1)
        else:
            player.update_action(0)
        player.move(moving_left, moving_right)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                moving_left = True
            if event.key == pygame.K_d:
                moving_right = True
            if event.key == pygame.K_SPACE:
                shoot = True
            if event.key == pygame.K_q:
                grenade = True
            if event.key == pygame.K_w and player.alive:
                player.jump = True
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                moving_left = False
            if event.key == pygame.K_d:
                moving_right = False
            if event.key == pygame.K_SPACE:
                shoot = False
            if event.key == pygame.K_ESCAPE:
                run = False
            if event.key == pygame.K_q:
                grenade = False
                grenade_thrown = False

    pygame.display.update()

pygame.quit()