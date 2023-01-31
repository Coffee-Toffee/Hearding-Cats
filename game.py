# SETUP # -----------------------------------------------
import sys, random, os 
import pygame as pg
from classes import * 
from threading import Thread

BLACK = (0,0,0)
DGREEN = (6,70,24)
PLAYER_SPEED = 3.3
ROOT_PATH = os.path.abspath(os.path.dirname(__file__))
print(ROOT_PATH)


# INIT # ------------------------------------------------
size = (width,height) = (1000,1400)
screen = pg.display.set_mode(size)
pg.init()

cat = Cat()
cat.set_image("cat.png")

player = Player(-1)
player.set_image("catgirl.png")
player.set_pos((250,250))

test = Static(-1, (100,100))
test.set_image("cat.png")

allsprites = pg.sprite.RenderPlain(cat, player, test)



# GAME LOGIC # ------------------------------------------
while True:
    
    for event in pg.event.get():
        if event.type == pg.QUIT: sys.exit()
    
    if pg.key.get_pressed()[pg.K_w]: player.forward(PLAYER_SPEED)
    if pg.key.get_pressed()[pg.K_a]: player.left(PLAYER_SPEED)
    if pg.key.get_pressed()[pg.K_s]: player.backward(PLAYER_SPEED)
    if pg.key.get_pressed()[pg.K_d]: player.right(PLAYER_SPEED)

    screen.fill(DGREEN)
    allsprites.update()
    allsprites.draw(screen)
    pg.display.flip()
