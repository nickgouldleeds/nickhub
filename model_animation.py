import time
import agentframework
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot
import matplotlib.animation 


start = time.clock()

num_of_agents = 15
num_of_iterations = 100
agents = []

fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])


f = open("in.txt")
environment = []
for line in f:
    parsed_line = str.split(line,",")
    #print (parsed_line)
    rowlist = [] 
    for word in parsed_line:
        rowlist.append(float(word))
    environment.append(rowlist)
f.close()
tot_env_start = 0
for i in range(len(environment)):
    for j in range(len(environment[i])):
        tot_env_start += environment[i][j]
print ("starting food",tot_env_start)

#matplotlib.pyplot.imshow(environment)
#matplotlib.pyplot.show()
#
#matplotlib.pyplot.xlim(0, 99)
#matplotlib.pyplot.ylim(0, 99)

# Make the agents...
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment,agents))

# plot the starting positions
#for i in range(num_of_agents):
#    matplotlib.pyplot.scatter(agents[i].getx(),agents[i].gety(),color='red')

def update(frame_number):
    # Move the agents,eat,share...

    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(2) # share with other agents that are within n units
        matplotlib.pyplot.scatter(agents[i].getx(),agents[i].gety(),facecolors='none', edgecolors='black')



#matplotlib.pyplot.imshow(environment)
#matplotlib.pyplot.show()



animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, repeat=False, frames=num_of_iterations) 

#matplotlib.pyplot.imshow(environment)


tot_env_end = 0
for i in range(len(environment)):
    for j in range(len(environment[i])):
        tot_env_end += environment[i][j]
print ("ending food",tot_env_end)
print ("food eaten",tot_env_start - tot_env_end)

end = time.clock()
print("time = " + str(end - start))

#testing getting and setting
#my_agent = agentframework.Agent()
#print (my_agent.getx(),my_agent.gety())
#my_agent.setx(23)
#my_agent.sety(43)
#print (my_agent.getx(),my_agent.gety())
#for agents_row_a in agents:
#    for agents_row_b in agents:
#        distance = distance_between(agents_row_a, agents_row_b) 

