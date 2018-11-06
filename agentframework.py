import random
class Agent(object):
    def __init__(self,environment,agents,object_id):
        self._y = random.randint(0,99)
        self._x = random.randint(0,99)
        self._object_id = object_id
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

    def share_with_neighbours(self, neighbourhood):
         share_count = 0
         for agent in self.agents:
             if agent._object_id != self._object_id:
                 dist = self.distance_between(agent) 
                 if dist <= neighbourhood:
                     sum = self.store + agent.store
                     ave = sum /2
                     self.store = ave
                     agent.store = ave
                     #print("sharing " + str(dist) + " " + str(ave))
                     share_count += 1
         print ("total shared with",share_count)
      
    def distance_between(self, agent):
        return (((self._x - agent._x)**2) + ((self._y - agent._y)**2))**0.5 
 

