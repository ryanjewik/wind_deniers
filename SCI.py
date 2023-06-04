import requests
import os
from datetime import datetime

def WindDeny():
    BASE_URL = "http://api.openweathermap.org/data/2.5/forecast?"
    API_key = "77402ec4c492f560257042cd7325b413"
    City = "Orange"
    url = BASE_URL + "appid=" + API_key + "&q=" + City


    def KelvintoFahrenheit(kelvin):
        celsius = kelvin - 273.15
        fahrenheit = celsius * (9/5) +32
        return celsius,fahrenheit


    response = requests.get(url).json()

    #tempKelvin = response['system']['main']['temp']
    #tempCelsius,tempFahrenheit = KelvintoFahrenheit(tempKelvin)
    #print("temperature in {City} is {tempKelvin}" )


    listThing = response.get('list')
    bigListThing = []
    for i in range(len(listThing)):
        #print (listThing[i])
        dictlistThing = listThing[i]
        main = dictlistThing.get('main')


        newListThing = []
        temp = main.get('temp')
        pressure = main.get('pressure')
        humidity = main.get('humidity')
        time = dictlistThing.get('dt_txt')
        print("temp: " + str(temp))
        print("pressure: " + str(pressure))
        print("humidity: " + str(humidity))
        print("time: " + str(time))
        print("_____________________________________________")
        newListThing.append(temp)
        newListThing.append(pressure)
        newListThing.append(humidity)
        newListThing.append(time)
        bigListThing.append(newListThing)


    #return(bigListThing)

print(WindDeny())
