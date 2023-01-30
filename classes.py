import pygame as pg
import random

class Player(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.pos = (0,0)
    
    def set_image(self, Sprite):
        self.image = pg.image.load(Sprite)
        self.rect = self.image.get_rect()

    def forward(self, speed):
        self.pos = (self.pos[0], self.pos[1]-speed*0.1)
    def backward(self, speed):
        self.pos = (self.pos[0], self.pos[1]+speed*0.1)
    def left(self, speed):
        self.pos = (self.pos[0]-speed*0.1, self.pos[1])
    def right(self, speed):
        self.pos = (self.pos[0]+speed*0.1, self.pos[1])
   


    def set_pos(self,pos):
        self.pos = pos

    def update(self):
        #self.pos = pg.mouse.get_pos()
        #self.pos = list(map(lambda x: int(x), self.pos))
        self.rect.topleft = list(map(lambda x: int(x+50), self.pos))
 

class Cat(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.pos = (0,0)
        self.i=0
    def set_image(self, Sprite):
        self.image = pg.image.load(Sprite)
        self.rect = self.image.get_rect()

    def wander(self, move, sleepy):
        if (move):
            pg.time.wait(sleepy)
            pos = ((self.pos[0] + random.randrange(-5, 5)), (self.pos[1] + random.randrange(-5, 5)))
        else: 
            pos = self.pos
        return(pos)
    
    def set_pos(self,pos):
        self.pos = pos

    def update(self):
        #self.pos = pg.mouse.get_pos()
        #self.pos = self.wander(True, 350)  
        #self.pos = list(map(lambda x: (x+1), self.pos))
        self.rect.topleft = list(map(lambda x: int(x), self.pos))
        #self.i+=1
        pass
