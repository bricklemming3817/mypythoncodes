counter = 0
while counter <= 0:
    x = int(input("number ?"))


    def factorial(x):
        if x == 1 or x == 0:
            return 1
        else:
            p = x * (factorial(x - 1))
            return p


    print(factorial(x))
counter += 1








