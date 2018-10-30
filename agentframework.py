import random
class Agent(object):
    def __init__(self,environment):
        self._y = random.randint(0,99)
        self._x = random.randint(0,99)
        self.environment = environment
        self.store = 0
    def getx(self):
         return self._x
    def gety(self):
         return self._y
    
    def setx(self,x):
         self._x = x
    def sety(self,y):
         self._y = y
    
    def eat(self): # can you make it eat what is left?
       if self.environment[self._y][self._x] > 10:
           self.environment[self._y][self._x] -= 10
           self.store += 10 
        
    def move(self):
        if random.random() < 0.5:
            self._y = (self._y + 1) % 100
        else:
            self._y = (self._y - 1) % 100

        if random.random() < 0.5:
            self._x = (self._x + 1) % 100
        else:
            self._x = (self._x - 1) % 100

