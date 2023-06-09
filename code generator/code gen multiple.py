import tkinter as tk
import ttkbootstrap as ttk
import random 

# CO NASTEPNE: 
# 1. Po kliknieciu enter wyswietla sie wynik.
# 2. Jak tekst wyjdzie za okienko to zeby okno samo sie powiększało.
# 3. Żeby dało sie skopiować kod..
# 4. Dwa okienka, jedno zwykłe że tylko wpisujesz długość, drugie wybierasz dokładną ilość znaków.


# Code generator

def randomcode():
    h_m_s = input_small_letters_int.get()
    small_letters = list(''.join(random.choice('abcdefghijklmnoprstuwz')for i in range(h_m_s)))

    h_m_b = input_big_letters_int.get()
    big_letters = list(''.join(random.choice('ABCDEFGHIJKLMNOPRSTUWZ')for i in range(h_m_b)))
    
    h_m_n = input_numbers_int.get()
    numbers = list(''.join(random.choice('1234567890')for i in range(h_m_n)))
    
    h_m_s = input_signs_int.get()
    signs = list(''.join(random.choice('!@#$%^&*')for i in range(h_m_s)))

    code = small_letters + big_letters + numbers + signs

    random.shuffle(code)
    
    output_string.set(code)


# Window 

window = ttk.Window(themename='darkly')
window.title("Anrunt's code gen")
window.geometry('450x350')


# Title 

title_label = ttk.Label(master = window,text = 'Code Generator', font = 'Calibri 20 bold')

how_many_s_l = ttk.Label(master = window, text = 'How many small letters:', font = 'Calibri 12')


title_label.pack()
how_many_s_l.pack()

# Input frame
input_letters_frame = ttk.Frame(master=window)

# Small letters
input_small_letters_int = tk.IntVar()
input_small_letters = ttk.Entry(master = input_letters_frame, textvariable= input_small_letters_int)

# Big Letters

how_many_b_l = ttk.Label(master = input_letters_frame, text = 'How many big letters:', font = 'Calibri 12')
input_big_letters_int = tk.IntVar()
input_big_letters = ttk.Entry(master = input_letters_frame, textvariable = input_big_letters_int)

# Numbers

how_many_n = ttk.Label(master = input_letters_frame, text='How many numbers:', font = 'Calibri 12')
input_numbers_int = tk.IntVar()
input_numbers = ttk.Entry(master = input_letters_frame, textvariable = input_numbers_int)

# Signs

how_many_s = ttk.Label(master = input_letters_frame, text = 'How many signs:', font = 'Calibri 12')
input_signs_int = tk.IntVar()
input_signs = ttk.Entry(master=input_letters_frame, textvariable = input_signs_int)

# Button

button = ttk.Button(master=input_letters_frame, text = 'Generate Code', 
command = randomcode)

# All packs

input_letters_frame.pack()
input_small_letters.pack()

how_many_b_l.pack()
input_big_letters.pack()

how_many_n.pack()
input_numbers.pack()

how_many_s.pack()
input_signs.pack()

button.pack(pady=10)


# Output 

output_string = tk.StringVar()
output_Label = ttk.Label(master = window,text = 'output', font = 'Calibri 20',
textvariable = output_string )

output_Label.pack()

# Run 
window.mainloop()
