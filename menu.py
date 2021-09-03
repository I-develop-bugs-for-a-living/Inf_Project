import pygame
import os
import pygame_menu

pygame.init()

Surface=pygame.display.set_mode((400,300))

menu = pygame_menu.Menu("Cooles Game" , 400, 300, theme=pygame_menu.themes.THEME_DARK)
menu.add.text_input("Name: ", default= "Hubi")
menu.add.selector("Härtegrad:", [("Leicht",1), ("Hart", 2)])
menu.add.button("Start", start_the_game)

menu.mainloop(Surface)