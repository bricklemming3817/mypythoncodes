import numpy as np

upper_limit = 2
lower_limit = 0


def function(x):
    return x ** 2


if upper_limit == 1 and lower_limit == -1:
    final_intergal = function(3 ** (-0.5)) + function(-(3 ** (-0.5)))

else:
    a = 2 / (upper_limit - lower_limit)
    b = -1 * a * (upper_limit + lower_limit) / 2


    def new_function(t):
        return (function((t - b) / a)) / a


    final_intergal = new_function(3 ** (-0.5)) + new_function(-(3 ** (-0.5)))

print("integral of the function", "from", lower_limit, "to", upper_limit, "=", final_intergal)
