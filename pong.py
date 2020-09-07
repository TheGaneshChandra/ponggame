#my pong pygame

import pygame

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

pygame.init()

score = 0
size = (500,500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("my pong")

#paddle initial coordinates
rectx = 300
recty = 480

#speed of paddle
rectxspd = 0
rectyspd = 0

#initial position of ball
balx = 50
baly = 50

#speed of ball
balxspd = 5
balyspd = 5

#paddle draw work
def drawrect(screen,x,y):
    if x <= 0:
        x = 0
    if y <= 0:
        y = 0
    pygame.draw.rect(screen,GREEN,[x,y,80,20])

#game main code
may = True
clk = pygame.time.Clock()

while may:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            may = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                rectxspd = -6
            if event.key == pygame.K_RIGHT:
                rectxspd = 6
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                rectxspd = 0
            #elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                #rect_change_y = 0

    screen.fill(BLACK)
    rectx += rectxspd
    recty += rectyspd
    balx  += balxspd
    baly  += balyspd

    #movement of ball
    if balx < 0:
        balx = 0
        balxspd = balxspd*-1
    elif balx > 485:
        balx = 485
        balxspd = balxspd*-1
    elif baly < 0:
        baly = 0
        balyspd = balyspd*-1
    elif balx > rectx and balx < rectx + 100 and baly == 465:
        balyspd = balyspd*-1
        score = score+1
    elif baly > 499:
        balyspd = balyspd*-1
        score = 0
    pygame.draw.rect(screen,WHITE,[balx, baly, 15, 15])

    drawrect(screen,rectx,recty)

    #font
    font = pygame.font.SysFont('Calibri', 15, False, False)
    text = font.render("Score = " + str(score), True, WHITE)
    screen.blit(text,[300,300])

    pygame.display.flip()#updates entire screen but pygame.display.update() only updates specific parts

    clk.tick(60)

pygame.quit()
