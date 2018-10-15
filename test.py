#print ("Hello Andy how are you today!")

import random
x0 = 50
y0 = 50
print("x0", x0)
print("y0", y0)
x1 = 50
y1 = 50
print("x1", x1)
print("y1", y1)

random_number = random.random()
print("random_number", random_number)

# Change x0 by a small amount
if random_number < 0.5:
     x0 = x0 + 1
     print("added 1 to x0")
else:
     x0 = x0 - 1
     print("subtracted 1 to x0")
print("x0", x0)

# Change y0 by a small amount
if random_number < 0.5:
     y0 = y0 + 1
     print("added 1 to y0")
else:
     y0 = y0 - 1
     print("subtracted 1 from y0")
print("y0", y0)

# Calculate the distance between (x0, y0) and (x1, y1)
distance = (((y0 - y1)**2) + ((x0 - x1)**2))**0.5
print("distance between (x0, y0) and (x1, y1)", distance)
     
