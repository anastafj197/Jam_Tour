#https://stackoverflow.com/questions/42579927/rounded-button-tkinter-python
#state shaped buttons 

import fetch

from fetch import state_dict
from fetch import bands

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

	else:
		state_dict[button['text']].selected = False 
		button.configure(bg = "grey")


btn_dict = {}

# Insert btns into a dictionary of buttons with 
# corresponding state names attached 
# seperate & color code by division 
def fill_btn_dict():
	
	y = 0
	x0,x1,x2,x3,x4,x5,x6,x7,x8 = (0,)*9
	
	for state in state_dict: 

		div = state_dict[state].division

		if div == "New England":		
			y = 0
			obj=Button(master, text=state, bg = "coral")
			obj.configure(command=lambda button=obj: highlight(button))
			btn_dict[state] = obj
			btn_dict[state].grid(row=x0, column=y)
			x0 += 1

		elif div == "Mid-Atlantic":
			y = 1
			obj=Button(master, text=state, bg = "gold")
			obj.configure(command=lambda button=obj: highlight(button))
			btn_dict[state] = obj
			btn_dict[state].grid(row=x1, column=y)
			x1 += 1

		elif div == "East North Central":
			y = 2
			obj=Button(master, text=state, bg = "greenyellow")
			obj.configure(command=lambda button=obj: highlight(button))
			btn_dict[state] = obj
			btn_dict[state].grid(row=x2, column=y)
			x2 += 1

		elif div == "West North Central":
			y = 3
			obj=Button(master, text=state, bg = "forestgreen")
			obj.configure(command=lambda button=obj: highlight(button))
			btn_dict[state] = obj
			btn_dict[state].grid(row=x3, column=y)
			x3 += 1

		elif div == "South Atlantic":
			y = 4
			obj=Button(master, text=state, bg = "mediumturquoise")
			obj.configure(command=lambda button=obj: highlight(button))
			btn_dict[state] = obj
			btn_dict[state].grid(row=x4, column=y)
			x4 += 1

		elif div == "East South Central":
			y = 5
			obj=Button(master, text=state, bg = "dodgerblue")
			obj.configure(command=lambda button=obj: highlight(button))
			btn_dict[state] = obj
			btn_dict[state].grid(row=x5, column=y)
			x5 += 1

		elif div == "West South Central":
			y = 6
			obj=Button(master, text=state, bg = "mediumslateblue")
			obj.configure(command=lambda button=obj: highlight(button))
			btn_dict[state] = obj
			btn_dict[state].grid(row=x6, column=y)
			x6 += 1

		elif div == "Mountain":
			y = 7
			obj=Button(master, text=state, bg = "orchid")
			obj.configure(command=lambda button=obj: highlight(button))
			btn_dict[state] = obj
			btn_dict[state].grid(row=x7, column=y)
			x7 += 1

		elif div == "Pacific":
			y = 8
			obj=Button(master, text=state, bg = "lightpink")
			obj.configure(command=lambda button=obj: highlight(button))
			btn_dict[state] = obj
			btn_dict[state].grid(row=x8, column=y)
			x8 += 1

def band_list():
	x = 0
	for band in bands:
		obj=Button(master, text=band, bg = "lavender")
		obj.configure(command=lambda button=obj: highlight(button))
		obj.grid(row=x, column=10)
		x += 1
		#print(band)

fill_btn_dict()
band_list()
mainloop()
