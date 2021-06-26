from matplotlib import pylab as plt
import numpy as np
import random
x = []
y = []
actual_pi = np.pi
iterations = 1
average_percentage_error = []
total_percentage_error = 0
n = 1000
counter = 0
def estimate_pi(n):
    circle_points = 0
    square_points = 0

    for i in range(n):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)

        if x ** 2 + y ** 2 <= 1:
            circle_points += 1
        square_points += 1

    pi = 4 * circle_points / square_points
    return pi


while counter <= 0:
    estimated_pi = estimate_pi(n)
    relative_error = abs(estimated_pi - actual_pi) / actual_pi
    percentage_error = relative_error * 100
    total_percentage_error += percentage_error
    average = (total_percentage_error/iterations)

    iterations += 1
    
    y.append(percentage_error)
    x.append(n)
    average_percentage_error.append(average)

    print("    ")
    print("estimated value of pi", estimated_pi)
    print("percentage error in", iterations-1, "th iteration is",percentage_error,"%")

    n += 10

    if percentage_error <= 0.001:
        break



print("number of points used:", n - 10)
print("Total number of iterations is", iterations-1)
print("avarage percentage error", average)

plt.plot(x,y, label = "percentage error")
plt.plot(x ,average_percentage_error, label = "average percentage error")
plt.xlabel("number of points")
plt.ylabel("percentage error/average error")
plt.grid()
plt.legend()

plt.show()

"""
PLEASE USE THIS SYNTAX INCASE TO MULTIPLOT


fig, axs = plt.subplots(2)
axs[0].plot(x,y)
axs[0].set_title("percentage error vs number of points")
axs[1].plot(x ,average_percentage_error, color = 'orange')
axs[1].set_title("avaerage percentage error vs number of points")

"""
















