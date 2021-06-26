from tkinter import *
import parser


root = Tk()
root.title("Leap Year Calculator")
def clear_all():
    display.delete(0,END)


def calculation():
    entire_string = display.get()

    try:
        a = int(entire_string)
        if a % 100 == 0:
            if (a % 400 == 0):
                clear_all()
                display.insert(0, entire_string + " is a leap-year!")
            else:
                clear_all()
                display.insert(0, entire_string + " is not a leap year!")




        elif a % 4 == 0:
            clear_all()
            display.insert(0, entire_string + " is a leap-year")
        else:
            clear_all()
            display.insert(0, entire_string + " is not a leap year")
    except Exception:
        display.insert(0,"Error404")




frame  = Frame(root)
frame.pack()

header = Label(frame , text = "Enter the year:" , relief = GROOVE)
header.grid(row = "0" , column = "0" )

display = Entry(frame)
display.grid(row = "0" , column = "1" , sticky = W+E)

button = Button(frame , text = "Check" , relief = GROOVE, padx = 30, command = lambda: calculation())
button.grid(row = 2 , column = 1)
root.mainloop()
