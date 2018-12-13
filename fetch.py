# Referance for the interactive state map 
# https://www.amcharts.com/visited_states/#

# Must find new database to fetch from 
# JamBase does not like scrapers  

from urllib.request import urlopen 
from bs4 import BeautifulSoup 

import pprint 

#html = urlopen("?")
#bsObj = BeautifulSoup(html, "lxml")

def fetch():

	base_url = "https://www.jambase.com/band/"

	# band names may need to be formatted differently 
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
			"lockn",
			"camp-bisco",
			"high-siera",
			"summer-camp",
			"mountain-jam",
			"gathering-of-the-vibes"
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
	def __init__(self, name, abv, selected, division):
		self.name = name 
		self.abv = abv 
		self.selected = False 
		self.division = division

	# toString 
	def __repr__( self ):
		return "" + self.name + ", " + self.abv + ", " + str(self.selected)

state_dict = {}

states = [
		"Alabama", "Alaska", "Arizona", "Arkansas", 
		"California", "Colorado", "Connecticut", 
		"Delaware", "Florida", 
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
		"AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", 
		"FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY",
		"LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT",
		"NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH",
		"OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT",
		"VT", "VA", "WA", "WV", "WI", "WY"
		]

regions = [
		  "New England",
		  "Mid-Atlantic",
		  "East North Central",
		  "West North Central",
		  "South Atlantic",
		  "East South Central",
		  "West South Central",
		  "Mountain",
		  "Pacific"
		  ]

# Filling a dictionary with state objects 
# Referancable by thier name 
def fill_dict():

	ix = 0 
	for state in states:		
		state_dict[states[ix]] = State(states[ix], abvs[ix], False, "none")
		ix += 1 

	pprint.pprint(state_dict)

def fill_division():
	
	new_england        = ["Connecticut", "Maine", "Massachusetts", "New Hampshire",
	 					  "Rhode Island", "Vermont"] 
	mid_atlantic       = ["New Jersey", "New York", "Pennsylvania"]
	east_north_central = ["Illinois", "Indiana", "Michigan", "Ohio", "Wisconsin"]
	west_north_central = ["Iowa", "Kansas", "Minnesota", "Missouri", "Nebraska", 
						  "North Dakota", "South Dakota"]
	south_atlantic     = ["Delaware", "Florida", "Georgia", "Maryland", "North Carolina", 
						  "South Carolina", "Virginia", "West Virginia"]
	east_south_central = ["Alabama", "Kentucky", "Mississippi", "Tennessee"] 
	west_south_central = ["Arkansas", "Louisiana", "Oklahoma", "Texas"]
	mountain           = ["Arizona", "Colorado", "Idaho", "Montana", "Nevada", "New Mexico", 
	 					  "Utah", "Wyoming"]
	pacific            = ["Alaska", "California", "Hawaii", "Oregon", "Washington"]



# this won't be run when imported
#if __name__ == "__main__":
#	main()

def main():
	fetch()
	fill_dict()
	fill_division()

main()
