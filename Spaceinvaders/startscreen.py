import pygame
import sys
from game import Game
from pygame.locals import *
import random

# init pygame
pygame.init()

# screensize
width, height = 1200, 900

# logo
logo = pygame.image.load("Icon/ufo.png")

# load spaceshipskins in
spaceship_skin1 = pygame.image.load("Spaceship/Spaceship1.png")
spaceship_skin2 = pygame.image.load("Spaceship/SpaceShip.png")
spaceship_skin3 = pygame.image.load("Spaceship/spaceship +.png")
spaceship_skin4 = pygame.image.load("Spaceship/shipspace.png")

# scale images
spaceship_skin1 = pygame.transform.scale(spaceship_skin1, (100, 100))
spaceship_skin2 = pygame.transform.scale(spaceship_skin2, (100, 100))
spaceship_skin3 = pygame.transform.scale(spaceship_skin3, (100, 100))
spaceship_skin4 = pygame.transform.scale(spaceship_skin4, (100, 100))


# diffrent bg`s
bg_list = [pygame.image.load("Bg/background.png"), pygame.image.load("Bg/space hole.png"), pygame.image.load("Bg/space pixl.png"), pygame.image.load("Bg/space.png")]
bg = random.choice(bg_list)

# music
pygame.mixer.music.load("Music/musicfox_roadstar.mp3")
pygame.mixer.music.play(-1)

# Clock for fps
mainClock = pygame.time.Clock()

# title and logo of screen
pygame.display.set_caption('Spaceinvaders')
pygame.display.set_icon(logo)

screen = pygame.display.set_mode((width, height), 0, 32)

# defining fonts
font_h1 = pygame.font.SysFont(None, 200)
font_h2 = pygame.font.SysFont(None, 40)
font_h3 = pygame.font.SysFont(None, 30)

 
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
 
click = False
 
def main_menu():
    while True:
        # draw on screen
        screen.blit(bg, (0, 0))
        draw_text('Spaceinvaders', font_h1, (255, 255, 255), screen, 100, 20)
        draw_text('Music by: www.musicfox.com ', font_h3, (255, 255, 255), screen, 10, 650)

        # get mouseposition
        mx, my = pygame.mouse.get_pos()

        # def button-position
        button_1 = pygame.Rect(500, 300, 200, 50)
        button_2 = pygame.Rect(500, 400, 200, 50)
        button_3 = pygame.Rect(500, 500, 200, 50)
        button_4 = pygame.Rect(500, 600, 200, 50)

        # if mouse collides with button
        if button_1.collidepoint((mx, my)):
            if click:
                game()
        
        if button_2.collidepoint((mx, my)):
            if click:
                options()
        
        if button_3.collidepoint((mx, my)):
            if click:
                shop()

        if button_4.collidepoint((mx, my)):
            if click:
                my_credits()

        # draw buttons
        pygame.draw.rect(screen, (255, 0, 0), button_1)
        pygame.draw.rect(screen, (255, 0, 0), button_2)
        pygame.draw.rect(screen, (255, 0, 0), button_3)
        pygame.draw.rect(screen, (255, 0, 0), button_4)

        
        # build textobjects
        textb1_object = font_h2.render("Play!", True, (0, 255, 0))
        textb2_object = font_h2.render("Options", True, (0, 255, 0))
        textb3_object = font_h2.render("Shop", True, (0, 255, 0))
        textb4_object = font_h2.render("Credits", True, (0, 255, 0))

        # blit textobjects into the buttons
        screen.blit(textb1_object, (570, 310))
        screen.blit(textb2_object, (570, 410))
        screen.blit(textb3_object, (570, 510))
        screen.blit(textb4_object, (570, 610))

        # get keyinputs
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
 
        pygame.display.update()
        mainClock.tick(60)

# start the main game
def game():
    pygame.init()
    # Game(num_enemies, boss_state=False, fps=30)
    g = Game(10, width, height)
    g.set_up()
    g.run()
 
# settings/options window
def options():
    running = True
    while running:
        screen.fill((0,0,0))
 
        draw_text('options', font_h1, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
        pygame.display.update()
        mainClock.tick(60)


# credits window
def my_credits():
    running = True
    while running:
        screen.fill((0,0,0))
 
        draw_text('credits', font_h1, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
       
        pygame.display.update()
        mainClock.tick(60)
 
def shop():
    running = True

    button_1 = pygame.Rect(50, 300, 200, 200)
    button_2 = pygame.Rect(350, 300, 200, 200)
    button_3 = pygame.Rect(650, 300, 200, 200)
    button_4 = pygame.Rect(950, 300, 200, 200)

    while running:
        screen.fill((0,0,0))
 
        draw_text('Customize your Spaceship!', font_h2, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        # draw boxes
        pygame.draw.rect(screen, (255, 0, 0), button_1)
        pygame.draw.rect(screen, (255, 0, 0), button_2)
        pygame.draw.rect(screen, (255, 0, 0), button_3)
        pygame.draw.rect(screen, (255, 0, 0), button_4)
        
        # draw the skins in the boxes
        screen.blit(spaceship_skin1, (100, 350))
        screen.blit(spaceship_skin2, (400, 350))
        screen.blit(spaceship_skin3, (700, 350))
        screen.blit(spaceship_skin4, (1000, 350))

        pygame.display.update()
        mainClock.tick(60)

#calling the mainfunction and starting the program
main_menu()
