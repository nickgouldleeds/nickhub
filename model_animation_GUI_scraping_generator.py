"""
Implements the agent framework buy creating agents with starting
locations determined from a scraped web page. Agents move randomly, eating the
environment and sharing with neighbours
"""
# added data scraping to set agent starting locations
# This works but still pops up an unwanted window (ony if we don't do inline graphics in Spyder.
# 
import sys
import time
import agentframework_scraping as agentframework
import matplotlib
import tkinter
matplotlib.use('TkAgg')
import matplotlib.pyplot
import matplotlib.animation 
import matplotlib.backends.backend_tkagg
import requests
import bs4
import random

start = time.process_time()

num_of_agents = 5
num_of_iterations = 100
agents = []

fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 100, 100])


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



#scrape a web page to get the agent starting locations...
r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
td_ys = soup.find_all(attrs={"class" : "y"})
td_xs = soup.find_all(attrs={"class" : "x"})

tot_env_start = 0
for i in range(len(environment)):
    for j in range(len(environment[i])):
        tot_env_start += environment[i][j]
print ("starting food",tot_env_start)
sys.stdout.flush()
# Make the agents...
for i in range(num_of_agents):
    #instead of random starting positions, use locations from scraped web page...
    y = int(td_ys[i].text)
    x = int(td_xs[i].text)    
    agents.append(agentframework.Agent(environment,agents,y,x))

carry_on = True	

def update(frame_number):
    #this is called by the matplot lib animation
    # Move the agents,eat,share...
    #new display...
    fig.clear()
    global carry_on
    
    #we want fixed axes (should we have to do this every time we clear the fig?!)...
    matplotlib.pyplot.xlim(0, 99)
    matplotlib.pyplot.ylim(0, 99)
    
    matplotlib.pyplot.imshow(environment)
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(2) # share with other agents that are within n units        
        #plot the agent...
        matplotlib.pyplot.scatter(agents[i].getx(),agents[i].gety(),facecolors='none', edgecolors='black')
    
    if random.random() < 0.01:
        carry_on = False
        print("random stopping condition")
        sys.stdout.flush()

def gen_function(b = [0]):
    
    a = 0
    global carry_on #Not actually needed as we're not assigning, but clearer
    while (a < 50) & (carry_on) :
        #https://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do                
        yield a			# Returns control and waits next call.
        a = a + 1
        print (a)
        sys.stdout.flush()
        
def run():
    # this is called by the GUI menu item 'Run'
    #animation = matplotlib.animation.FuncAnimation(fig, update, frames=num_of_iterations, repeat=False)
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
    canvas.draw()

#matplotlib.pyplot.imshow(environment)
#matplotlib.pyplot.show()
"""
Set-up the GUI using tkinter. Creates a window and a menu with a single menu
item.
"""
root = tkinter.Tk() 
root.wm_title("ABM Model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

#menubar = tkinter.Menu(root)
#filemenu = tkinter.Menu(menubar, tearoff=0)
#filemenu.add_command(label="Run", command=run)
#root.config(menu=menubar)


menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run)



root.mainloop()

#tkinter.mainloop() 


tot_env_end = 0
for i in range(len(environment)):
    for j in range(len(environment[i])):
        tot_env_end += environment[i][j]
print ("ending food",tot_env_end)
print ("food eaten",tot_env_start - tot_env_end)



