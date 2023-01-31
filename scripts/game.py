# SETUP # -----------------------------------------------
import sys, random, os 
import pygame as pg
from classes import * 
from threading import Thread

BLCK = (0,0,0)
DGRN = (6,70,24)
PLAYER_SPEED = 3.3
ROOT_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), "..")

def fetch_asset(file_name):
    return os.path.join(ROOT_PATH, "assets", file_name)


# INIT # ------------------------------------------------
size = (width,height) = (1000,1400)
screen = pg.display.set_mode(size)
pg.init()

cat = Cat()
cat.set_image(fetch_asset("cat.png"))

player = Player(-1)
player.set_image(fetch_asset("catgirl.png"))
player.set_pos((250,250))

test = Static(-1, (100,100))
test.set_image(fetch_asset("cat.png"))

allsprites = pg.sprite.RenderPlain(cat, player, test)



# GAME LOGIC # ------------------------------------------
while True:
    
    for event in pg.event.get():
        if event.type == pg.QUIT: sys.exit()
    
    if pg.key.get_pressed()[pg.K_w]: player.forward(PLAYER_SPEED)
    if pg.key.get_pressed()[pg.K_a]: player.left(PLAYER_SPEED)
    if pg.key.get_pressed()[pg.K_s]: player.backward(PLAYER_SPEED)
    if pg.key.get_pressed()[pg.K_d]: player.right(PLAYER_SPEED)

    screen.fill(DGRN)
    allsprites.update()
    allsprites.draw(screen)
    pg.display.flip()
