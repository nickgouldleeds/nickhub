import random
class Agent(object):
    """Provides a class for an agent that can move in space and interact
    with other agents and its environment        
    """ 
    def __init__(self,environment,agents,y,x):
        self._y = y # was random.randint(0,99)
        self._x = x # was random.randint(0,99)
        self.environment = environment
        self.agents = agents
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
       if self.environment[self._y][self._x] >= 40:
           self.environment[self._y][self._x] -= 40
           self.store += 40 
        
    def move(self):
        """
        Move an agent randomly in 2D
        """
        if random.random() < 0.5:
            self._y = (self._y + 1) % 100
        else:
            self._y = (self._y - 1) % 100

        if random.random() < 0.5:
            self._x = (self._x + 1) % 100
        else:
            self._x = (self._x - 1) % 100

    def share_with_neighbours(self, neighbourhood):
         for agent in self.agents:
             if agent != self: # don't want to share with myself
                 dist = self.distance_between(agent) 
                 if dist <= neighbourhood:
                     sum = self.store + agent.store
                     ave = sum /2
                     self.store = ave
                     agent.store = ave
                     #print("sharing " + str(dist) + " " + str(ave))
      
    def distance_between(self, agent):
        return (((self._x - agent._x)**2) + ((self._y - agent._y)**2))**0.5 
 