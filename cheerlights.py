
import time
from sys import exit
import requests
import unicornhat as uh

# set the layout
uh.set_layout(uh.PHAT)

# brightness
uh.brightness(0.5)

#number of transitions
steps = 20

# If you need proxy
proxies = {
	'http': '<proxy_address>:<port>',
	'https': '<proxy_address>:<port>'
}

def lightitup(oldr, oldg, oldb, r, g, b):
	curStep = 0

	# next we need to calculate the amount to increment (or decrement) 
	# for each individual color (R G B) from the old color to the new color in the number
	# of steps (transistions) defined above
	# ie:
		# old R color value: 146
		# new R color value: 16
		# abs is used to have positive values
		# stepa = abs (16 - 146) / 20 = 100 / 20 = 5
		# Which means, in each one of the 20 transistions, we will remove 5 from 146 - to arrive at 16 in 20 loops
	# This way, we will have a kind of gradient effect when changing colors
	
	stepa = abs(r - oldr) / steps
	stepg = abs(g - oldg) / steps
	stepb = abs(b - oldb) / steps
	
	# This is ugly, but I don't know the terneary operator in Python.
	# every attempt I've made did not work... 
	while (curStep < steps):
		if (oldr > r):
			oldr -= stepa
		else:
			oldr += stepa
		if (oldg > g):
			oldg -= stepg
		else:
			oldg += stepg
		if (oldb > b):
			oldb -= stepb
		else:
			oldb += stepb
		#print ("step: %s %s %s" % (oldr, oldg, oldb))
		for x in range(8):
			for y in range(4):
				uh.set_pixel(x, y, oldr, oldg, oldb)
		uh.show()
		time.sleep(0.01)
		curStep += 1

#borrowed from Pimoroni's Cheerlights from blink examples
def hex_to_rgb(col_hex):
	"""Convert hex color to rgb"""
	col_hex = col_hex.lstrip("#")
	return bytearray.fromhex(col_hex)

# first time, have to set colors
r = 0
b = 0
g = 0
while True:
	try:
		# with proxy
		req = requests.get("http://api.thingspeak.com/channels/1417/field/2/last.json", timeout=2,proxies=proxies)
		# without proxy
		#req = requests.get("http://api.thingspeak.com/channels/1417/field/2/last.json", timeout=2)
		# save old colors
		oldr = r
		oldg = g
		oldb = b
		r, g, b = hex_to_rgb(req.json()["field2"])

		#	print ("old colors: %s %s %s" % (oldr,oldg,oldb))
		#	print ("New colors: %s %s %s" % (r,g,b))

		lightitup(oldr, oldg, oldb, r, g, b)
		# Wait 10s before another request to the API - be friendly
		time.sleep(10)
	# added exception for when there's no connection 
	# it doesn't exit the app, but waits 10s and tries again
	except requests.exceptions.Timeout:
		time.sleep(10)
		# print ("no connection")
		continue
