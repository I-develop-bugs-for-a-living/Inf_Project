import pygame
import os
import pygame_menu
from pygame_menu import themes

difficulty_value = 0
difficulty_int = "None"

def set_variable(value, difficulty):
    global difficulty_int, difficulty_value
    difficulty_value = value
    difficulty_int = difficulty

def start():
    print(difficulty_value, difficulty_int)


pygame.init()

a = pygame_menu.font.FONT_8BIT

MyTheme = pygame_menu.themes.THEME_DARK.copy()

myimage = pygame_menu.baseimage.BaseImage(image_path="assets/bg/Background-Pic.jpg", 
drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL)

MyTheme.title_font = a

MyTheme.background_color = myimage

MyTheme.widget_font = a
MyTheme.widget_font_size = (40)
MyTheme.widget_font_color =(0,0,0)

MyTheme.widget_margin = (0,40)

Surface=pygame.display.set_mode((1000,700))

menu = pygame_menu.Menu("Cooles Game" ,1000 , 700, theme=MyTheme)
menu.add.text_input("Name: ", default= "Hubi")
menu.add.selector("Schwierigkeit:", [("Leicht",1), ("Hart", 2)], onchange=set_variable)
menu.add.button("Start", start)
menu.add.button("Ausgang", pygame_menu.events.EXIT)

menu.mainloop(Surface)