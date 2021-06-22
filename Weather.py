import requests
#import os
from datetime import datetime

api_key = '5e0ae3f4bc870b46b6b706778d157844'
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

#create variables to store and display data
temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

print ("-------------------------------------------------------------")
print ("Weather Stats for - {}  || {}".format(location.upper(), date_time))
print ("-------------------------------------------------------------")

print ("Current temperature is: {:.2f} deg C".format(temp_city))
print ("Current weather desc  :",weather_desc)
print ("Current Humidity      :",hmdt, '%')
print ("Current wind speed    :",wind_spd ,'kmph')

humdty = str(hmdt)
wspeed = str(wind_spd)

f = open("Text.txt", "a")
f.write("-------------------------------------------------------------\n")
f.write("Weather Stats for - {}  ".format(location.upper()))
f.write("date and time = {}".format(date_time))
f.write("\n-------------------------------------------------------------\n")
f.write("Current temperature is: {:.2f} deg C".format(temp_city) + "\n")
f.write("Current weather desc  :"+ weather_desc +"\n")
f.write("Current Humidity      :" + humdty + "%\n")
f.write("Current wind speed    :" + wspeed +" kmph\n")
f.close()
