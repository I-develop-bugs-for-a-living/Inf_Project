import pygame
import math

class BoxesGame():
    def __init__(self) -> None:
        pygame.init()
        self.boardh = [[False for x in range(6)] for y in range(7)]
        self.boardv = [[False for x in range(7)] for y in range(6)]
        width, heigth = 389, 489
        self.screen = pygame.display.set_mode((width, heigth))
        pygame.display.set_caption("Boxes")
        self.clock=pygame.time.Clock()
        self.initGraphics()

    def initGraphics(self):
        self.normallinev = pygame.image.load("normalline.png")
        self.normallineh = pygame.transform.rotate(pygame.image.load("normalline.png"), -90)
        self.bar_donev = pygame.image.load("bar_done.png")
        self.bar_doneh = pygame.transform.rotate(pygame.image.load("bar_done.png"), -90)
        self.hoverlinev = pygame.image.load("hoverline.png")
        self.hoverlineh = pygame.transform.rotate(pygame.image.load("hoverline.png"), -90)

    def update(self):
        self.clock.tick(60)
        self.screen.fill(0)
        self.drawBoard()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        mouse = pygame.mouse.get_pos()
        xpos = int(math.ceil((mouse[0]-32)/64.0))
        ypos = int(math.ceil((mouse[1]-32)/64.0))
        is_horizontal = abs(mouse[1]-ypos*64) < abs(mouse[0] - xpos*64)
        ypos = ypos - 1 if mouse[1] - ypos*64 < 0 and not is_horizontal else ypos
        xpos = xpos - 1 if mouse[0] - xpos*64 < 0 and is_horizontal else xpos
        board = self.boardh if is_horizontal else self.boardv
        isoutofbounds = False
        try:
            if not board[ypos][xpos]: 
                if not board[ypos][xpos]: 
                    self.screen.blit(self.hoverlineh if is_horizontal else self.hoverlinev, [xpos*64+5 if is_horizontal else xpos*64, ypos*64 if is_horizontal else ypos*64+5])
        except:
            isoutofbounds=True
            pass
        if not isoutofbounds:
            alreadyplaced=board[ypos][xpos]
        else:
            alreadyplaced=False

        pygame.display.flip()
    
    def drawBoard(self):
        for x in range(6):
            for y in range(7):
                if not self.boardh[y][x]:
                    self.screen.blit(self.normallineh, [(x)*64+5, (y)*64])
                else:
                    self.screen.blit(self.bar_doneh, [(x)*64+5, (y)*64])
        for x in range(7):
            for y in range(6):
                if not self.boardv[y][x]:
                    self.screen.blit(self.normallinev, [(x)*64, (y)*64+5])
                else:
                    self.screen.blit(self.bar_donev, [(x)*64, (y)*64+5])

bg = BoxesGame()
while 1:
    bg.update()


