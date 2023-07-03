import datetime as dt
import requests
import math
import tkinter as tk 
import customtkinter as ctk
from tkinter import ttk
from tkinter import messagebox


# main window 
window = ctk.CTk()
window.geometry('600x400')
window.title('Cloudly')

def get_weather(city):
    API_KEY = '862957c16730a84ba992b581fadd84e4'
    BASE_URL = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    response = requests.get(BASE_URL)

    if response.status_code == 404:
        messagebox.showerror("Error", "City not found")
        return None

    weather = response.json()
    temperature = weather['main']['temp'] - 273.15
    city = weather['name']
    return (city,temperature)

def search():
    city = search_bar.get()
    result = get_weather(city)

    if result is None:
        return
    
    city,temperature = result
    rounded_temperature = round(temperature,1)

    output_label.config(text=f"Temperature in {city} is {rounded_temperature}°C")


# Entry

search_bar = ctk.CTkEntry(window,width=200,corner_radius=20)
search_bar.pack()

# Button 
search_button = ctk.CTkButton(window,text='Show Weather',width=100,corner_radius=20,command=search)
search_button.pack(pady=10)

# output label 
output_label = ttk.Label(window,width=40)
output_label.pack(pady = 10)


window.mainloop()