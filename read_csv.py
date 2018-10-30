import matplotlib
f = open("in.txt")
environment = []
for line in f:
    parsed_line = str.split(line,",")
    print (parsed_line)
    rowlist = [] 
    for word in parsed_line:
        rowlist.append(float(word))
    environment.append(rowlist)
matplotlib.pyplot.imshow(environment)
matplotlib.pyplot.show()