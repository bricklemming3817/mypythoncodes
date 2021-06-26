import re
print("WELCOME TO MY TEXT FINDER/EDITOR")
print("PLEASE NOTE - answers to the question either YES/NO")
big_counter = 0
while big_counter <= 0:
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
                substitute = input("do you want to replace this word with some other word? ")
                if substitute == "yes":
                    new_pattern = input("enter the new word ")
                    new_string = re.sub(pattern , new_pattern , string )
                    file = open("new passage.txt" , 'w')
                    file.write(new_string)
                    file.close()
                    print("new passage has been saved as a text file in the folder")
                    print("Thank you")
                    quit = input("press x to close" )
                    if quit == "x":
                        exit()



        else:
            print("match not found, try again ")
            restart_new = input("do you want to try for another passage? ")
            if restart_new == "yes":
                break

    counter += 1
big_counter += 1
