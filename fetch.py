# Referance for the interactive state map 
# https://www.amcharts.com/visited_states/#

# Fetching data from jamBase.com 

from urllib.request import urlopen 
from bs4 import BeautifulSoup 

import pprint 

#html = urlopen("https://www.jambase.com/band/moe")
#bsObj = BeautifulSoup(html, "lxml")


def fetch():

	base_url = "https://www.jambase.com/band/"

	# band names to match jamBases urls 
	bands = [
			"dark-star-orchestra",
			"dead-company",
			"dopapod",
			"joe-russos-almost-dead",
			"lotus",
			"lettus",
			"max-creek",
			"moe",
			"phil-lesh-friends",
			"phish",
			"pigeons-playing-ping-pong",
			"tedeschi-trucks-band",
			"the-disco-biscuits",
			"the-motet",
			"the-string-cheese-incident",
			"the-werks",
			"trey-anastasio-band",
			"turkuaz",
			"twiddle",
			"umphreys-mcgee",
			"widespread-panic",
			]

	# festivals 
	festi = [
			"camp-bisco",
			"summer-camp",
			"lockn",
			"high-siera",
			]

	# urls to visit 
	urls = []

	# check if urls are being appended properly
	for band in bands:
		url = base_url + band
		urls.append(url)
		url = base_url
 
	print(urls)
	print()

class State:
	# May add on region in constructor 
	def __init__(self, name, abv, selected):
		self.name = name 
		self. abv = abv 
		self.selected = False 

	def __repr__( self ):
		return "" + self.name + ", " + self.abv + ", " + str(self.selected)

state_dict = {}

states = [
		"Alabama", "Alaska", "Arizona", "Arkansas", 
		"California", "Colorado", "Connecticut", 
		"Delaware", "District of Columbia", "Florida", 
		"Georgia", "Hawaii", "Idaho", "Illinois", "Indiana",
		"Iowa", "Kansas", "Kentucky", "Louisiana", "Maine",
		"Maryland", "Massachusetts", "Michigan", "Minnesota",
		"Mississippi", "Missouri", "Montana", "Nebraska",
		"Nevada", "New Hampshire", "New Jersey", "New Mexico",
		"New York", "North Carolina", "North Dakota", "Ohio",
		"Oklahoma", "Oregon", "Pennsylvania", "Rhode Island",
		"South Carolina", "South Dakota", "Tennessee",
		"Texas", "Utah", "Vermont", "Virginia", "Washington",
		"West Virginia", "Wisconsin", "Wyoming"
		 ]

abvs =  [
		"AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "DC",
		"FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY",
		"LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT",
		"NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH",
		"OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT",
		"VT", "VA", "WA", "WV", "WI", "WY"
		]

# attempting to make a new state obj for each state 
ix = 0 
for state in states:		
	state_dict[states[ix]] = State(states[ix], abvs[ix], False)
	ix += 1 

pprint.pprint(state_dict)
