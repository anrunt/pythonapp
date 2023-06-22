import tkinter as tk
import ttkbootstrap as ttk
import random
import pyperclip 


# Basic Random Code

def randomcode_press():
    code_length = entry_letters_int.get()
    code = list(''.join(random.choice("ABCDEFGHIJKLMNOPRSTUWabcdefghijklmnoprstuwz1234567890!@#$%^&*")for i in range(code_length))) 
    random.shuffle(code)

    output_string1.set(code)

def randomcode(event):
    code_length = entry_letters_int.get()
    code = list(''.join(random.choice("ABCDEFGHIJKLMNOPRSTUWabcdefghijklmnoprstuwz1234567890!@#$%^&*")for i in range(code_length))) 
    random.shuffle(code)

    output_string1.set(code)


# Pro Random Code

def randomcode_pro_press():
    how_many_s_l = small_l_int.get()
    small_letters = list(''.join(random.choice('abcdefghijklmnoprstuwz')for i in range(how_many_s_l)))

    how_many_b_l = big_l_int.get()
    big_letters = list(''.join(random.choice('ABCDEFGHIJKLMNOPRSTUWZ')for i in range(how_many_b_l)))
    
    how_many_n = numbers_int.get()
    numbers = list(''.join(random.choice('1234567890')for i in range(how_many_n)))
    
    how_many_s = signs_int.get()
    signs = list(''.join(random.choice('!@#$%^&*')for i in range(how_many_s)))

    code = small_letters + big_letters + numbers + signs

    random.shuffle(code)
    
    output_string.set(code)

def randomcode_pro(event):
    how_many_s_l = small_l_int.get()
    small_letters = list(''.join(random.choice('abcdefghijklmnoprstuwz')for i in range(how_many_s_l)))

    how_many_b_l = big_l_int.get()
    big_letters = list(''.join(random.choice('ABCDEFGHIJKLMNOPRSTUWZ')for i in range(how_many_b_l)))
    
    how_many_n = numbers_int.get()
    numbers = list(''.join(random.choice('1234567890')for i in range(how_many_n)))
    
    how_many_s = signs_int.get()
    signs = list(''.join(random.choice('!@#$%^&*')for i in range(how_many_s)))

    code = small_letters + big_letters + numbers + signs

    random.shuffle(code)
    
    output_string.set(code)




# Window 
window = ttk.Window(themename='darkly')
window.geometry('450x390')
window.title("Anrunt's code generator")

# Notebook widget 

notebook = ttk.Notebook(window)

# Tab 1 - Random code Basic
tab1 = ttk.Frame(notebook)

# Title 1

title_Label1 = tk.Label(tab1, text = "Code Generator", font = 'Calibri 20')
title_Label1.pack()

how_many_Label = tk.Label(tab1, text = 'Enter code length:', font ='Calibri 12')
how_many_Label.pack()

# Input Frame 1

input_frame2 = tk.Frame(tab1)
input_frame2.pack()


entry_letters_int = tk.IntVar()
entry_letters = ttk.Entry(master= input_frame2, textvariable=entry_letters_int)

entry_letters.bind('<Return>', randomcode)

entry_letters.focus()
entry_letters.pack()


# Button 1 Generate
button1 = tk.Button(tab1, text = 'Generate', command = randomcode_press)
button1.pack(pady=10)

# Button 1 Copy
buttonC = tk.Button(tab1, text = 'Copy', command = lambda: pyperclip.copy(str(output_string1.get())))
buttonC.pack()

# Output 1

output_string1 = tk.StringVar()
output_Label1 = ttk.Label(tab1, font = 'Calibri 15', textvariable=output_string1)

output_Label1.pack(pady=5)


# Tab 2 - Random code Pro 
tab2 = ttk.Frame(notebook)

# Title 2
title_label = ttk.Label(tab2, text = 'Code Generator', font = 'Calibri 20 bold')

title_label.pack()

# Input Frame 2

input_frame = ttk.Frame(tab2)

input_frame.pack()

# Small letters 2

how_many_s_l = ttk.Label(master = input_frame, text = 'How many small letters:', font = 'Calibri 12 bold')
small_l_int = tk.IntVar()
input_small_letters = ttk.Entry(master = input_frame, textvariable = small_l_int)

input_small_letters.bind('<Return>', randomcode_pro)

how_many_s_l.pack()
input_small_letters.pack()

# Big letters 2

how_many_b_l = ttk.Label(master = input_frame, text = "How many big letters:",font = 'Calibri 12 bold')
big_l_int = tk.IntVar()
input_big_letters = ttk.Entry(master = input_frame, textvariable=big_l_int)

input_big_letters.bind('<Return>', randomcode_pro)

how_many_b_l.pack()
input_big_letters.pack()

# Numbers 2

how_many_n = ttk.Label(master = input_frame, text = 'How many numbers',font = 'Calibri 12 bold')
numbers_int = tk.IntVar()
input_numbers = ttk.Entry(master = input_frame, textvariable = numbers_int)

input_numbers.bind('<Return>', randomcode_pro)

how_many_n.pack()
input_numbers.pack()
 
# Signs 2
how_many_s = ttk.Label(master = input_frame, text = 'How many signs:', font = 'Calibri 12 bold')
signs_int = tk.IntVar()
input_signs = ttk.Entry(master = input_frame, textvariable = signs_int)

input_signs.bind('<Return>', randomcode_pro)

how_many_s.pack()
input_signs.pack()

# Button 2 Generate

button = ttk.Button(master = input_frame, text = 'Generate', command = randomcode_pro_press)
button.pack(pady=10)

# Button 2 Copy
buttonC2 = tk.Button(tab2, text='Copy', command = lambda: pyperclip.copy(str(output_string.get())))
buttonC2.pack()
# Output 2

output_string = tk.StringVar()
output_label = ttk.Label(tab2,font = 'Calibri 20', textvariable = output_string)

output_label.pack()
# Notebook add 

notebook.add(tab1, text = 'Basic')
notebook.add(tab2, text = 'Pro')
notebook.pack()

# Run 
window.mainloop()