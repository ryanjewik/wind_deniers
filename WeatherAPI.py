import requests
import os 
from datetime import datetime 


BASE_URL = "http://api.openweathermap.org/data/2.5/forecast?"
API_key = "77402ec4c492f560257042cd7325b413"
City = "Orange"
url = BASE_URL + "appid=" + API_key + "&q=" + City


def KelvintoFahrenheit(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = celsius * (9/5) +32
    return celsius,fahrenheit


response = requests.get(url).json()

#print ("response['humidity']: ", response['message'])
#temp_min = response['list']['temp_min']

list_length = len(response['list'])
print(list_length)
temp_min = response['list'][0]['main']['temp_min']
print(temp_min)
#289.62 for 0
#289.71 for 23
#288.87 for 24
#287.57 for 25
#def dicReturn(dictKey):
 #   return 

#tempKelvin = response['Weather']['temp']
#tempCelsius,tempFahrenh eit = KelvintoFahrenheit(tempKelvin)


#print("temperature in {City} is {tempKelvin}" )
#print(response)