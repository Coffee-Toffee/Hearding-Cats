# SETUP # -----------------------------------------------
from threading import Thread #Todo
import sys, os
import pygame as pg
from classes import * 

BLCK = (0,0,0)
DGRN = (6,70,24)
SPEED_PLAYER = 3.3
PATH_ROOT = os.path.join(os.path.abspath(os.path.dirname(__file__)), "..")

def fetch_asset(file_name: str) -> str:
    return os.path.join(PATH_ROOT, "assets", file_name)


# INIT # ------------------------------------------------
size = width,height = (1000,1400)
screen = pg.display.set_mode(size)
pg.init()

level = 1
cats = []

#all sprites get `img, strength = 0, pos = (0,0)`. 
# Static() gets `shown = 0`, Cat() gets `cat_type=0`

for i in range(level*2):
    cats.append(Cat(img = fetch_asset("cat.png"), pos =(i*10,i*10), strength=-1))
    pass

#cat = Cat(img = fetch_asset("cat.png")) 
player = Player(pos = (250, 250), strength = -5, img = fetch_asset("catgirl.png"))
test = Static(pos = (100,100), img = fetch_asset("cat.png"))

allsprites = pg.sprite.RenderPlain(*cats, player, test)


# GAME LOGIC # ------------------------------------------
while True:
    
    for event in pg.event.get():
        if event.type == pg.QUIT: sys.exit()
    
    if pg.key.get_pressed()[pg.K_w]: player.forward(SPEED_PLAYER)
    if pg.key.get_pressed()[pg.K_a]: player.left(SPEED_PLAYER)
    if pg.key.get_pressed()[pg.K_s]: player.backward(SPEED_PLAYER)
    if pg.key.get_pressed()[pg.K_d]: player.right(SPEED_PLAYER)

    screen.fill(DGRN)
    allsprites.update()
    allsprites.draw(screen)
    pg.display.flip()
