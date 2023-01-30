import sys, random 
import pygame as pg
from classes import * 
pg.init()

size = width, height =1000 , 1400
speed = [2,-1]
black = 0,0,0
dgreen = 6,70,24

modulus = 10

screen = pg.display.set_mode(size)
#cat = pygame.image.load("cat.png")
#catrect = cat.get_rect()
loop = 0
cat = Cat()
cat.set_image("cat.png")

player = Player()
player.set_image("catgirl.png")
player.set_pos((250,250))
speed = 3.3

allsprites = pg.sprite.RenderPlain(cat, player)
while True:

    for event in pg.event.get():
        if event.type == pg.QUIT: sys.exit()
        
    if pg.key.get_pressed()[pg.K_w] : player.forward(speed)
    if pg.key.get_pressed()[pg.K_a] : player.left(speed)
    if pg.key.get_pressed()[pg.K_s] : player.backward(speed)
    if pg.key.get_pressed()[pg.K_d] : player.right(speed)

        

    '''
    if loop%modulus == 0:
        catrect = catrect.move(speed)
        if catrect.left < 0 or catrect.right > width :
            speed[0] = -speed[0]
    
    if catrect.top < 0:
        catrect.top = height
    '''

    screen.fill(dgreen)
    allsprites.update()
    allsprites.draw(screen)
    pg.display.flip()

