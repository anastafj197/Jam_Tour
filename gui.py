import fetch

from tkinter import *

master = Tk()

def highlight():
	exit()

# Accepts Tk object, btn name, and function 
button = Button(master, text = "State", command = highlight)

# Need to pack every button made 
button.pack()

mainloop()
