#Assignment 1 Weather app by Carlos Canales
import requests
import tkinter
import customtkinter
from customtkinter import *

def GetData():
    #From OpenWeathermap website
    Api = '3fc4eeee3662c136aa450763fc7e54b8'

    zipcode = entryBlock.get()
    exclude = "minute, hourly"
    weatherData = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?zip={zipcode}&units=imperial&APPID={Api}")

    data = weatherData.json()

    name = data['name']
    lon = data['coord']['lon']
    lat = data['coord']['lat']

    url = requests.get(f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&units=imperial&appid={Api}")

    data2 = url.json()

    descrip = [] 
    days = []
    
    for i in range(5):
        days.append(round(data2['list'][i]['main']['temp']))
        descrip.append(data2['list'][i]['weather'][0]['main'])

    # weather = weatherData.json()['weather'][0]['description']
    # temper = weatherData.json()['main']['temp']
    city.configure(text="5 Day Forcast for the City of " + name +".")
    OutputWeather.configure(text = "Weather: " + descrip[0] + " | " + descrip[1] + " | "+ descrip[2] + " | "+ descrip[3] + " | "+ descrip[4])
    OutputTemp.configure(text = "Temperature: " + str(days[0]) + "°F | "+ str(days[1]) + "°F | "+ str(days[2]) + "°F | "+ str(days[3]) + "°F | "+ str(days[4]) + "°F")

app = customtkinter.CTk()
app.geometry("750x400")
app._set_appearance_mode("system")
app.title("Get Weather info based on Zip Code - US Only")

label = CTkLabel(app, text="Please enter Zip Code", text_color="white", font=('defualt', 20,'bold'))
label.pack(padx = 10, pady = 10)

userInput = tkinter.StringVar()
entryBlock = CTkEntry(app, width=300, height=50, textvariable=userInput, justify = CENTER, font=('defualt', 20,'bold'))
entryBlock.pack(padx = 10, pady = 10)

button = customtkinter.CTkButton(app, text="my button", command=GetData)
button.pack(padx=20, pady=20)

city = CTkLabel(app, text="",  font=('defualt', 20))
city.pack(padx=10, pady=10)

OutputTemp = CTkLabel(app, text="" , font=('defualt', 20))
OutputTemp.pack(padx=10, pady=10)

OutputWeather = CTkLabel(app, text="",  font=('defualt', 20))
OutputWeather.pack(padx=10, pady=10)

app.mainloop()