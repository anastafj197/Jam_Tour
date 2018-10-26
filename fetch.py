# Fetching data from jamBase.com 

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
