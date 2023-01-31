import sys, random 
import pygame as pg
from classes import * 
from threading import Thread

pg.init()

size = width, height =1000 , 1400
speed = [2,-1]
black = 0,0,0
dgreen = 6,70,24

player_speed = 3.3
#modulus = 10

screen = pg.display.set_mode(size)

loop = 0

cat = Cat()
cat.set_image("cat.png")

player = Player(-1)
player.set_image("catgirl.png")
player.set_pos((250,250))

test = Static(-1, (100,100))
test.set_image("cat.png")


allsprites = pg.sprite.RenderPlain(cat, player, test)

while True:

    for event in pg.event.get():
        if event.type == pg.QUIT: sys.exit()
    
    speed = player_speed
    if pg.key.get_pressed()[pg.K_w] : player.forward(speed)
    if pg.key.get_pressed()[pg.K_a] : player.left(speed)
    if pg.key.get_pressed()[pg.K_s] : player.backward(speed)
    if pg.key.get_pressed()[pg.K_d] : player.right(speed)

    screen.fill(dgreen)
    allsprites.update()
    allsprites.draw(screen)
    pg.display.flip()
