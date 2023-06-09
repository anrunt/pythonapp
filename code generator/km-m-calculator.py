import tkinter as tk
import ttkbootstrap as ttk

def convert():
    mile_input = entry_Int.get()
    km_output = mile_input * 1.61
    
    output_string.set(km_output)

# window 

window = ttk.Window(themename = 'darkly')
window.title("Miles to km conv")
window.geometry("300x150")

# title

title_label= ttk.Label(
    master = window, 
    text = "Miles to km", 
    font = ' Calibri 20 bold')
title_label.pack()

# input field

input_frame = ttk.Frame(master = window)

entry_Int = tk.IntVar()
entry = ttk.Entry(
    master = input_frame,
    textvariable = entry_Int)

button = ttk.Button(
    master = input_frame, 
    text ='Convert', 
    command = convert)

entry.pack(side = 'left', padx = 5)
button.pack(side = 'left', pady = 10)

input_frame.pack()

# output
output_string = tk.StringVar()
output_Label = ttk.Label(
    master = window, 
    text = 'Output', 
    font = 'Calibri 15', 
    textvariable = output_string)

output_Label.pack(pady=5)

# run
window.mainloop()
