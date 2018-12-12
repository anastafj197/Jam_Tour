#https://stackoverflow.com/questions/42579927/rounded-button-tkinter-python
#state shaped buttons 

import fetch

from fetch import state_dict
from tkinter import *

master = Tk()

def highlight(button):

	# if selected is false turn true 
	# must referance the buttons name 
	# compare against the state_dict 

	# Switch for selected boolean 
	if state_dict[button['text']].selected == False:
		state_dict[button['text']].selected = True 
		button.configure(bg = "steel blue")
		#print("T")
	else:
		state_dict[button['text']].selected = False 
		button.configure(bg = "grey")
		#print("F")

btn_dict = {}

# Insert btns into a dictionary of buttons with 
# corresponding state names attached 
def fill_btn_dict():
	x = 0
	y = 0
	for state in state_dict: 
		obj=Button(master, text=state, bg = "grey")
		obj.configure(command=lambda button=obj: highlight(button))

		btn_dict[state] = obj
		btn_dict[state].grid(row=x, column=y)

		x += 1
		if x == 5:
			y += 1
			x = 0

fill_btn_dict()

mainloop()
