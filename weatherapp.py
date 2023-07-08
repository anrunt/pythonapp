import requests
import tkinter as tk
from tkinter import ttk
import math
from tkinter import messagebox
from PIL import Image, ImageTk
import ttkbootstrap as ttk

def get_weather(city):
        API_KEY = '862957c16730a84ba992b581fadd84e4'
        BASE_URL = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"

        result = requests.get(BASE_URL)
    

        if result.status_code == 404:
            messagebox.showerror("Error", "City not found")
            return None

        weather = result.json()
        temperature = weather['main']['temp'] - 273.15
        city = weather['name']
        sky = weather['weather'][0]['description']
        icon_id = weather['weather'][0]['icon']
        humidity = weather['main']['humidity']
        windspeed = weather['wind']['speed']
        # importing image
        icon_url = f"http://openweathermap.org/img/wn/{icon_id}@2x.png"
    
        return (city, temperature, sky, icon_url, humidity, windspeed)

def search():
        
        city = entry.get()
        result = get_weather(city)

        (city, temperature, sky, icon_url, humidity, windspeed) = result # type:ignore 

        image = Image.open(requests.get(icon_url, stream=True).raw)
        icon = ImageTk.PhotoImage(image)
        icon_label.configure(image=icon)
        icon_label.image = icon # type:ignore

        round_temp = round(temperature, 1)

        city_name_label.configure(text=city)

        temperature_label.configure(text=f"Temperature: {round_temp}°C")

        appearance_label.configure(text=sky)

        humidity_label.configure(text=f"Humidity: {humidity}%")

        wind_speed_label.configure(text=f"Wind Speed: {windspeed} m/s")
        



class App(ttk.Frame):
    def __init__(self,parent):
        super().__init__(parent)
        self.pack(expand=True,fill='both')

        global entry
        global city_name_label
        global temperature_label
        global icon_label
        global appearance_label
        global humidity_label
        global wind_speed_label

        # search your city label
        ttk.Label(self, text='Enter your city name: ',font=('Arial', 20)).pack()

        # search
        entry = tk.Entry(self,font=('Arial', 22))
        entry.pack(pady=10)

        # button
        search_button = tk.Button(self,height=2,width=20, text='Search',command=search)
        search_button.pack(pady=5)

        # labels 
        city_name_label = tk.Label(self, text="", font=('Arial', 20))
        city_name_label.pack(pady=10)

        temperature_label = tk.Label(self, text="", font=('Arial', 20))
        temperature_label.pack(pady=10)

        icon_label = tk.Label(self)
        icon_label.pack()

        appearance_label = tk.Label(self, text="", font=('Arial', 20))
        appearance_label.pack()

        humidity_label = tk.Label(self,text="",font=('Arial',13))
        humidity_label.place(relx=0.082,rely=0.9)

        wind_speed_label = tk.Label(self,text='',font=('Arial',13))
        wind_speed_label.place(relx=0.5, rely=0.9)

        

# main 
weatherapp = ttk.Window('Cloudly',themename='vapor')
weatherapp.geometry('400x500')

# widgets
App(weatherapp)

# run 
weatherapp.mainloop()
