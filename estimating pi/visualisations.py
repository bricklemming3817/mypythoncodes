from matplotlib import pylab as plt
import random
n = 10000
m = 1000
x = []
y = []
p1 = []
p2 = []

for i in range(n):
    a = random.uniform(0,1)
    b = (1-(a**2))**0.5
    x.append(a)
    y.append(b)
plt.scatter(x,y, color = "k")

for j in range(m):
    gp1 = random.uniform(0,1)
    gp2 = random.uniform(0,1)
    p1.append(gp1)
    p2.append(gp2)

    plt.scatter(p1,p2)
    plt.pause(0.00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001)

plt.show()