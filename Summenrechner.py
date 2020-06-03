from tkinter import *
import numpy as np
import matplotlib.pyplot as plt
import math

pi = math.pi
e = math.e

def sin(x):
    return math.sin(x)
def cos(x):
    return math.cos(x)
def tan(x):
    return math.tan(x)

def asin(x):
    return math.asin(x)
def acos(x):
    return math.acos(x)
def atan(x):
    return math.atan(x)

def factorial(x):
    return math.factorial(x)

def log(x, base):
    return math.log(x, base)


counter = 0
def calculate_F():
    X = np.arange(int(from_E.get()), int(to_E.get())+1)
    sum = 0
    i = 0
    while i < (int(to_E.get())+1)-int(from_E.get()):
        x = float(X[i])
        sum += eval(function_E.get())
        i += 1

    global counter
    counter += 1
    global text_T
    text_T.insert(END, str(counter) + ". Sum of: " + str(function_E.get()) + " from x = " + str(from_E.get()) + " to x = " + str(to_E.get()) + " = " + str(sum) + "\n")


def plot_F():
    X = np.arange(int(from_E.get()), int(to_E.get()) + 1)
    Y = np.zeros((int(to_E.get())+1)-int(from_E.get()))
    sum = 0
    i = 0

    while i < (int(to_E.get())+1) - int(from_E.get()):
        x = float(X[i])
        if i == 0:
            Y[i] = eval(function_E.get())
        else:
            Y[i] = Y[i-1] + eval(function_E.get())
        i += 1

    global counter
    counter += 1
    global text_T
    text_T.insert(END, str(counter) + ". Sum of: " + str(function_E.get()) + " from x = " + str(from_E.get()) + " to x = " + str(to_E.get()) + " = " + str(Y[-1]) + "\n")

    plt.plot(X,Y, label = str(function_E.get()) + " from x = " + str(from_E.get()) + " to x = "+ str(to_E.get()))
    plt.legend()
    plt.show()

def clear_F():
    global counter
    counter = 0
    global text_T
    text_T.delete(1.0,END)

def clear_plot_F():
    plt.close()



menu = Tk()
menu.title("Summenrechner")

function_F = Frame(menu)
function_F.pack()
function_L = Label(function_F, text = "Sum of x")
function_E = Entry(function_F)
function_L.pack(side = LEFT)
function_E.pack(side = RIGHT)

from_F = Frame(menu)
from_F.pack()
from_L = Label(from_F, text = "from x =")
from_E = Entry(from_F)
from_L.pack(side = LEFT)
from_E.pack(side = RIGHT)

to_F = Frame(menu)
to_F.pack()
to_L = Label(to_F, text = "to x =")
to_E = Entry(to_F)
to_L.pack(side = LEFT)
to_E.pack(side = RIGHT)


top = Frame(menu)
top.pack()
bottom = Frame(menu)
bottom.pack()
calc_B = Button(top, text = "calculate", command = calculate_F)
calc_B.pack(side = LEFT)
clear_B = Button(bottom, text = "clear results", command = clear_F)
clear_B.pack(side = LEFT)
plot_B = Button(top, text = "plot", command = plot_F)
plot_B.pack(side = RIGHT)
clear_plot_B = Button(bottom, text = "clear plot", command = clear_plot_F)
clear_plot_B.pack(side = RIGHT)

text_T = Text(menu, height = 20, width = 60)
text_T.pack()



menu.mainloop()