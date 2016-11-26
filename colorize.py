import requests
import random

url = "https://query.yahooapis.com/v1/public/yql?q=select%20item.condition%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22budapest%2C%20hu%22)%20and%20u%3D'c'&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys"

request = requests.get(url)

#print r.status_code  #check back the status code (should be 200)

respone = request.json()
created = respone['query']['created']
text = respone['query']['results']['channel']['item']['condition']['text']
temp = respone['query']['results']['channel']['item']['condition']['temp']

# Dictionary for the results provided by API
result = {}
winterColors = {}
springColors = {}

#push the results into the dictionary

result = {'created' : created, 'text' : text}
winterColors = {'color1' : '#00275A', 'color2' : '#1862a2', 'color3' : '#B0B0B0', 'color4' : '#FFFFFF'}
autumnColors = {'color1' : '#7A0218', 'color2' : '#BF0426', 'color3' : '#EB6709', 'color4' : '#F7A305', 'color5' : '#FFD624'}
summerColors = {'color1' : '#16E811', 'color2' : '#13FF52', 'color3' : '#73FF20', 'color4' : '#ACE811', 'color5' : '#FFFA13'}
springColors = {'color1' : '#2FFF9D', 'color2' : '#FFEA55', 'color3' : '#96FF98', 'color4' : '#50909C', 'color5' : '#E5AD4A'}

# for keys,values in result.items():
#     print(keys)
#     print(values)

def createColorsForWeather (result):
	global random
	random = random.choice(winterColors.values())
	print random


createColorsForWeather (result)