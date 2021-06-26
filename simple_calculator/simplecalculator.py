from tkinter import *
import tkinter.messagebox
import parser


root = Tk()
root.title("Simple Calculator")



#Functions used
#Input Numberes
i = 0


def numbers(num):
    global i
    display.insert(i , num )
    i += 1
#clear all
def clear_all():
    display.delete(0,END)
#backspace
def delete():
    entire_string = display.get()
    if len(entire_string) > 0:
        new_string = entire_string[:-1]
        clear_all()
        display.insert(0,new_string)
    else:
        pass
# operators
def operation(operator):
    global i
    entire_string = display.get()
    length = len(entire_string)
    display.insert(i,operator)
    i += length



#calculation
def calculation():
    entire_string = display.get()
    try:
        a = parser.expr(entire_string).compile()
        result = eval(a)
        clear_all()
        display.insert(0, result)
    except Exception:
        clear_all()
        display.insert(0,"error")


#BODY-input
display = Entry(root)
display.grid(rowspan = 2 , columnspan = 5 , sticky = W+E)



#BODY-Number keys
Button(root , text = "0", relief = FLAT, padx = 15, command = lambda: numbers(0)).grid(row = "7" , column = "2")
Button(root , text = "1", relief = FLAT, padx = 15, command = lambda: numbers(1)).grid(row = "6" , column = "1")
Button(root , text = "2", relief = FLAT, padx = 15, command = lambda: numbers(2)).grid(row = "6" , column = "2")
Button(root , text = "3", relief = FLAT, padx = 15, command = lambda: numbers(3)).grid(row = "6" , column = "3")
Button(root , text = "4", relief = FLAT, padx = 15, command = lambda: numbers(4)).grid(row = "5" , column = "1")
Button(root , text = "5", relief = FLAT, padx = 15, command = lambda: numbers(5)).grid(row = "5" , column = "2")
Button(root , text = "6", relief = FLAT, padx = 15, command = lambda: numbers(6)).grid(row = "5" , column = "3")
Button(root , text = "7", relief = FLAT, padx = 15, command = lambda: numbers(7)).grid(row = "4" , column = "1")
Button(root , text = "8", relief = FLAT, padx = 15, command = lambda: numbers(8)).grid(row = "4" , column = "2")
Button(root , text = "9", relief = FLAT, padx = 15, command = lambda: numbers(9)).grid(row = "4" , column = "3")

#BODY - Other keys
Button(root , text = ".", relief = FLAT, padx = 15, command = lambda: operation(".")).grid(row = "7", column = "1")
Button(root , text = "(", relief = FLAT, padx = 15, command = lambda: operation("(")).grid(row = "7", column = "3")
Button(root , text = ")", relief = FLAT, padx = 15, command = lambda: operation(")")).grid(row = "7", column = "4")
Button(root , text = "=", relief = FLAT, padx = 15, command = lambda: calculation() ).grid(row = "7", column = "5")
Button(root , text = "+", relief = FLAT, padx = 15, command = lambda: operation("+")).grid(row = "6", column = "4")
Button(root , text = "-", relief = FLAT, padx = 15, command = lambda: operation("-")).grid(row = "6", column = "5")
Button(root , text = "x", relief = FLAT, padx = 15, command = lambda: operation("*")).grid(row = "5", column = "4")
Button(root , text = "/", relief = FLAT, padx = 15, command = lambda: operation("/")).grid(row = "5", column = "5")
Button(root , text = "^2", relief = FLAT, padx = 15, command = lambda: operation("**2")).grid(row = "4", column = "4")
Button(root , text = "exp", relief = FLAT, padx = 15, command = lambda: operation("**")).grid(row = "4", column = "5")
Button(root , text = "<-", relief = GROOVE, padx = 35, command = lambda: delete()).grid(row = "3", column = "2", columnspan = "2")
Button(root , text = "AC", relief = GROOVE, padx = 35, command = lambda: clear_all()).grid(row = "3", column = "4" , columnspan = "2")
Button(root , text = "pi", relief = FLAT, padx = 15, command = lambda: operation("*3.1416")).grid(row = "3", column = "1")


root.mainloop()
