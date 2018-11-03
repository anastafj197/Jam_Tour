import gui 
import fetch
import pprint 

from fetch import state_dict

# extract data from selected states 

my_states = []

for state in state_dict:
	if state_dict[state].selected == True:
		print(state)

	#if state.selected == true: 
		#my_bands.append(state)

#pprint.pprint(state_dict)

# Will run after the choice is made on gui 
# For which states are selected 

# To do:
# Button in gui.py to verify choices return the selected bands 

# Festivals
# associate:
# festival with state its held in 
# festival with most commonly attended bands
