import re
big_counter = 0
while big_counter<=0:
    string = input("enter the passage ")
    counter = 0
    while counter <= 0:
        pattern = input("enter the keyword ")
        if re.search(pattern, string):
            print("Match Found")
            y = re.findall(pattern, string)
            z = y.count(pattern)
            print("number of ", pattern, "in the passage is ", z)
            restart = input("do you want to search for a new passage? ")
            if restart == "yes":
                break
                

        else:
            print("match not found, try again ")
            restart_new = input("do you want to try for another passage? ")
            if restart_new == "yes":
                break

    counter += 1
big_counter += 1
