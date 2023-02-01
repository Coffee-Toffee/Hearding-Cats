import pygame as pg
import random
import numpy as np


class Sprite(pg.sprite.Sprite):
    
    def __init__(self, img, strength = 0, pos = (0,0)):
        pg.sprite.Sprite.__init__(self)
        self.strength = strength #str pos for an attractor, neg for detractor
        self.pos = np.array(pos)
        self.image = pg.image.load(img)
        self.rect = self.image.get_rect()


class Player(Sprite):
    
    '''
    Todo: actual movement system
    '''
    
    def __init__(self, img, strength = 0, pos = (0,0)):
        super().__init__(img, strength, pos)

    def forward(self, speed):
        self.pos = (self.pos[0], self.pos[1]-speed*0.1)
    def backward(self, speed):
        self.pos = (self.pos[0], self.pos[1]+speed*0.1)
    def left(self, speed):
        self.pos = (self.pos[0]-speed*0.1, self.pos[1])
    def right(self, speed):
        self.pos = (self.pos[0]+speed*0.1, self.pos[1])

    def update(self):
        self.rect.topleft = list(map(lambda x: int(x+50), self.pos))


class Static(Sprite):
    
    '''
    For anything that doesn't move, eg. fences, powerups, the corral

    Todo: collision system eventualy
    '''
    
    def __init__(self, img, strength = 0, pos = (0,0), shown = 0):
        super().__init__(img, strength, pos)
        self.shown = shown
            
    def show(self):
        self.rect.topleft = list(map(lambda x: int(x), self.pos))
    def update(self):
        if not self.shown:
            self.show() 
            self.shown = 1


class Cat(Sprite):

    '''
    Todo: implement a movement system for the cats
    '''
   
    TYPES = ["Default", "Lazy", "Crazy"] # Just some examples
    
    def __init__(self, img, strength = 0, pos = (0,0), cat_type = 0):
        super().__init__(img, strength, pos)
        self.type = self.TYPES[cat_type] 

    def wander(self, move, sleep_time):
        if (move):
            pg.time.wait(sleep_time)
            pos = ((self.pos[0] + random.randrange(-5, 5)), (self.pos[1] + random.randrange(-5, 5)))
        else: 
            pos = self.pos
        return(pos)

    def update(self):
        #self.pos = self.wander(True, 350)  
        self.pos = list(map(lambda x: (x+0.1*random.random()), self.pos))
        self.rect.topleft = list(map(lambda x: int(x), self.pos))
        pass
