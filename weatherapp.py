import requests
import tkinter as tk
from tkinter import ttk
import math
from tkinter import messagebox
from PIL import Image, ImageTk
import ttkbootstrap


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
    sky = weather['weather'][0]['main']
    icon_id = weather['weather'][0]['icon']

    # importing image
    icon_url = f"http://openweathermap.org/img/wn/{icon_id}@2x.png"

    return (city, temperature, sky, icon_url)


def search():
    city = entry.get()
    result = get_weather(city)

    (city, temperature, sky, icon_url) = result # type:ignore 

    image = Image.open(requests.get(icon_url, stream=True).raw)
    icon = ImageTk.PhotoImage(image)
    icon_label.configure(image=icon)
    icon_label.image = icon # type:ignore

    round_temp = round(temperature, 1)

    city_name_label.configure(text=city)

    temperature_label.configure(text=f"Temperature: {round_temp}°C")

    appearance_label.configure(text=sky)


# main
window = ttkbootstrap.Window(themename="vapor")
window.geometry('400x500')
window.title('Cloudly')

# Entry
entry = tk.Entry(window, font=('Arial', 22))
entry.pack(pady=5)

# Button
search_button = tk.Button(window,height=2,width=20, text='Search', command=search)
search_button.pack(pady=5)

city_name_label = tk.Label(window, text="", font=('Arial', 20))
city_name_label.pack(pady=10)

temperature_label = tk.Label(window, text="", font=('Arial', 20))
temperature_label.pack(pady=10)

icon_label = tk.Label(window)
icon_label.pack(pady=10)

appearance_label = tk.Label(window, text="", font=('Arial', 20))
appearance_label.pack(pady=10)

# run
window.mainloop()
