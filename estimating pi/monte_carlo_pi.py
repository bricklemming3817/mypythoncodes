import random
import numpy as np
from matplotlib import pylab as plt
n = 1000
a = []
b = []
PI = np.pi
p1 = []
p2 = []

for i in range(1000):
    gp1 = random.uniform(0,1)
    gp2 = (1-(gp1**2))**0.5


    p1.append(gp1)
    p2.append(gp2)


def estimate_pi(n):
    circle_points = 0
    square_points = 0

    for i in range(n):
        x = random.uniform(0,1)
        y = random.uniform(0,1)
        a.append(x)
        b.append(y)

        if x**2 + y**2<=1:
            circle_points+=1
        square_points += 1

    pi = 4*circle_points/square_points
    return(pi)
estimated_pi = estimate_pi(n)
relative_error = abs(estimated_pi-PI)/PI
percentage_error = relative_error*100


print("estimated value of pi: ", estimated_pi)
print("percentage error: ",percentage_error,"%")

plt.scatter(a,b, marker = 1)
plt.scatter(p1,p2, color = "k")
plt.grid()
plt.show()



