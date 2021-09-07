import pygame
import os
import pygame_menu
from pygame_menu import themes

pygame.init()

a = pygame_menu.font.FONT_8BIT

MyTheme = pygame_menu.themes.THEME_DARK.copy()
MyTheme.title_background_color=(180, 30, 180,99)
MyTheme.title_font = a

MyTheme.background_color = (170,20,20,99)
MyTheme.widget_font = a
MyTheme.widget_margin = (0,30)

Surface=pygame.display.set_mode((1000,700))

menu = pygame_menu.Menu("Cooles Game" ,1000 , 700, theme=MyTheme)
menu.add.text_input("Name: ", default= "Hubi")
menu.add.selector("Schwierigkeit:", [("Leicht",1), ("Hart", 2)])
menu.add.button("Start",)
menu.add.button("Ausgang", pygame_menu.events.EXIT)

menu.mainloop(Surface)