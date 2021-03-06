#!/usr/bin/env python

import requests
import random
from datetime import date, datetime
import matplotlib.colors as colors

url = "https://query.yahooapis.com/v1/public/yql?q=select%20item.condition%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22budapest%2C%20hu%22)%20and%20u%3D'c'&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys"

request = requests.get(url)

#print r.status_code  #check back the status code (should be 200)

Y = 2000 # dummy leap year to allow input X-02-29 (leap day)

seasons = [('winter', (date(Y,  1,  1),  date(Y,  3, 20))),
           ('spring', (date(Y,  3, 21),  date(Y,  6, 20))),
           ('summer', (date(Y,  6, 21),  date(Y,  9, 22))),
           ('autumn', (date(Y,  9, 23),  date(Y, 12, 20))),
           ('winter', (date(Y, 12, 21),  date(Y, 12, 31)))]


respone = request.json()
created = respone['query']['created']
text = respone['query']['results']['channel']['item']['condition']['text']
#print text
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

rainyColors = {'color1' : '#d8e3e9', 'color2' : '#788589', 'color3' : '#7b8b8a', 'color4' : '#e7e7e7', 'color5' : '#aba69f'}
snowingColors = {'color1' : '#ececf4', 'color2' : '#93add6', 'color3' : '#84baea', 'color4' : '#488cd8', 'color5' : '#0d53a7'}
cloudyColors = {'color1' : '#9c6c3a', 'color2' : '#1f221e', 'color3' : '#9da5ab', 'color4' : '#4c4b06'}

# for keys,values in result.items():
#     print(keys)
#     print(values)

def get_season(now):
    if isinstance(now, datetime):
        now = now.date()
    now = now.replace(year=Y)
    return next(season for season, (start, end) in seasons
                if start <= now <= end)

def createColors (result):
  global random
  random = random.choice(winterColors.values())
  return random

def getColorForSeason (season):
  if season == "autumn":
    seasonColor = autumnColors
  elif season == "winter":
    seasonColor = winterColors
  elif season == "summer":
    seasonColor = summerColors
  elif season == "spring":
    seasonColor = springColors
  return seasonColor

def getColorForWeather(text):
  if text == "Mostly Cloudy":
    weatherColor = cloudyColors
    print weatherColor

def hex_to_rgb(hex_string):
  rgb = colors.hex2color(hex_string)
  return tuple([int(255*x) for x in rgb])

currentSeason = get_season(date.today())

#print currentSeason

#print (getColorForSeason(currentSeason))

print (getColorForWeather(text))

#print (hex_to_rgb("#d8e3e9"))