import tkinter as tk
from tkinter import ttk
from math import pow
import customtkinter as ctk
from PIL import Image,ImageTk

# ZRÓB : 
# 1. WYJEB CANVASA I ZRÓB TO LABELAMI/ uzyj fixa z uilearning!!!
 





def get_result():

        result = float(kg_entry_str.get()) / pow((float(m_entry_str.get())),2)
        rounded_result = round(result,2) 
        output_label_str.set(float((rounded_result)))
        
        if rounded_result > 0:
            
            def show_full_image(event):
                global resized_tk

                # Current ratio
                canvas_ratio = event.width / event.height

                # Get coordinates
                if canvas_ratio > image_ratio:
                    height = int(event.height)
                    width = int(height* image_ratio)
                else:
                    width = int(event.width)
                    height = int(width / image_ratio)
                
                resized_image = image_original.resize((width,height))
                resized_tk = ImageTk.PhotoImage(resized_image)
                canvas.create_image(
                    int(event.width / 2),
                    int(event.height / 2),
                    anchor = 'center',
                    image = resized_tk)
                
                                       
            extra_window = tk.Toplevel()
            extra_window.geometry('470x265')
            extra_window.title('Tak wyglądasz')

            # Grid layout

            extra_window.columnconfigure((0,1,2,3),weight = 1, uniform = 'a')
            extra_window.rowconfigure(0,weight = 1)

            # Importing image
            image_original = Image.open('gigachad2.jpg')
            image_ratio = image_original.size[0] / image_original.size[1]
            image_tk = ImageTk.PhotoImage(image_original)


            # Canvas image
            canvas = tk.Canvas(extra_window, background='black', bd = 0, highlightthickness = 0, relief = 'ridge')
            canvas.grid(column = 0, columnspan = 4, row = 0, sticky = 'nsew')

            canvas.bind('<Configure>', show_full_image)



# Setup 
window = ctk.CTk()
window.config(highlightbackground='#000000')
window.geometry('400x300')
window.title('BMI CALCULATOR')


# Canvas 
canvas = tk.Canvas(window, width = 400, height = 300, background = '#000000',bd = 0, highlightthickness = 0,relief = 'ridge')
canvas.pack()

canvas.create_text((190,20), text='BMI CALCULATOR', font='Arial 20',fill='green')

canvas.create_text((80,60), text='Enter your weight:', font='Arial 12',fill='green')

canvas.create_text((113,120), text='Enter your height in meters:', font='Arial 12',fill='green')


kg_entry_str = ctk.StringVar()
m_entry_str = ctk.StringVar()

# Define entry boxes and output
kg_entry = ctk.CTkEntry(
    window,
    width=100,
    textvariable = kg_entry_str,
    fg_color='green',
    text_color='yellow',
    corner_radius=10)

m_entry = ctk.CTkEntry(
    window,
    width = 100,
    textvariable = m_entry_str,
    fg_color='green',
    text_color='yellow',
    corner_radius=10)

button = ctk.CTkButton(
    window,
    corner_radius=10,
    text='Calculate',
    fg_color = 'green',
    text_color = 'yellow',
    hover_color= 'blue',
    width=100,
    command = get_result)

output_label_str = ctk.StringVar()
output_label =ctk.CTkLabel(
    window,
    font = ('Arial', 18),
    width = 100,
    fg_color='#000000',
    textvariable = output_label_str)

# Adding entry boxes to the canvas - to musisz wyjebac ;) / albo bawic sie w fixa z uilearning
kg_entry_window = canvas.create_window((190,90),window = kg_entry)
m_entry_window = canvas.create_window((190,150),window = m_entry)
output_label_window = canvas.create_window((190,180), window=output_label)
button_window = canvas.create_window((190,210),window=button )


# Run 
window.mainloop()