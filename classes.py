import pygame as pg
import random


class Sprite(pg.sprite.Sprite):
    def __init__(self):
        self.strength = 0 #str pos for an attractor, neg for detractor
        pg.sprite.Sprite.__init__(self)
        self.pos = (0,0)

    def set_strength(self, strength):
        self.strength = strength 

    def get_strength(self):
        return(self.strength)

    def set_image(self, Sprite):
        self.image = pg.image.load(Sprite)
        self.rect = self.image.get_rect()

    def set_pos(self,pos):
        self.pos = pos


class Player(Sprite):
    '''
    Todo: actual movement system
    '''
    def __init__(self, strength): 
        Sprite.__init__(self)
        self.set_strength(strength)

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

    collision system eventualy, but is decent framework
    '''
    def __init__(self, strength, pos):
        Sprite.__init__(self)
        self.set_strength(strength)
        self.set_pos(pos)
        self.shown = 0

    def show(self):
        self.rect.topleft = list(map(lambda x: int(x), self.pos))
    def update(self):
        if not self.shown:
            self.show() 
            self.shown = 1

class Cat(Sprite):
    def wander(self, move, sleep_time):
        '''
        Todo: implement a movement system for the cats
        Future ideas:
        different types of cats, with different patterns
        of behaviors, so that way it's more interesting
        '''
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
