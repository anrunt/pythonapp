import tkinter as tk
import ttkbootstrap as ttk
import random

def randomcode():
    code_length = entry_letters_int.get()
    code = list(''.join(random.choice("ABCDEFGHIJKLMNOPRSTUWabcdefghijklmnoprstuwz1234567890!@#$%^&*")for i in range(code_length))) 
    random.shuffle(code)

    output_string.set(code)
    
randomcode.bind('<Return>',randomcode)    

# window

window = ttk.Window(themename='darkly')
window.title = "Anrunt's code generator"
window.geometry("300x170")

# title 

title_label = ttk.Label(
    master = window, 
    text = "Code Generator", 
    font = 'Calibri 20 bold')

how_many_Label = ttk.Label(
    master = window,
    text = 'Enter code length:',
    font = 'Calibri 12' )

title_label.pack()
how_many_Label.pack()

# input area

input_letters_frame = ttk.Frame(master = window)


entry_letters_int = tk.IntVar()
enter_letters = ttk.Entry(
    master = input_letters_frame,
    textvariable = entry_letters_int)


button = ttk.Button(
    master = input_letters_frame, 
    text = "Generate",
    command = randomcode )

enter_letters.pack(side = 'left', padx=10)
button.pack(side = 'left',pady=10)
input_letters_frame.pack()


# output

output_string = tk.StringVar()
output_Label = ttk.Label(
    master = window,
    text = 'Output',
    font = 'Calibri 15',
    textvariable = output_string)
    
output_Label.pack(pady=5)

#run 

window.mainloop()