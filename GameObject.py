import random as rdm

def randomColor():
        return (rdm.randint(0, 255), rdm.randint(0, 255), rdm.randint(0, 255))

class GameObject:
    def __init__(self, xspeed, yspeed):
        self.color = (0, 0, 0)
        self.xspeed = xspeed
        self.yspeed = yspeed
        self.pos = [0, 0]
        
    def move(self):
        self.pos[0] += self.xspeed
        self.pos[1] += self.yspeed 
        
        if self.pos[0] >= 725 or self.pos[0] <=0:
            self.xspeed= self.xspeed * (-1)
            self.color= randomColor()
            
        if self.pos[1] >= 725 or self.pos[1] <=0:
            self.yspeed= self.yspeed* (-1) 
            self.color= randomColor()
            
        print(self.pos)
    