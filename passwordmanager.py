import tkinter as tk
from tkinter import ttk
import ttkbootstrap
import random 
import pyperclip
from tkinter.font import Font

# Entry field
def create_tab1(parent,label_text,button_text):
    tab1 = ttk.Frame(master = parent)
    
    def append_to_treeview():
        password_name = password_name_str.get()
        login = login_str.get()
        password = password_str.get()
        data = (password_name,login,password)

        data_table.insert(parent='', index=0, values=data)

    ttk.Label(
        tab1,
        text=label_text,
        font= big_font).pack(pady=5)
    
    ttk.Label(
        tab1,
        text='Password Name',
        font=small_font).pack()

    password_name_str = tk.StringVar()
    password_name = ttk.Entry(tab1,width=30,textvariable=password_name_str)
    password_name.pack(pady=1)

    ttk.Label(
        tab1,
        text='Login',
        font = small_font).pack()

    login_str = tk.StringVar()
    login = ttk.Entry(tab1,width=30,textvariable=login_str)
    login.pack(pady=1)

    ttk.Label(
        tab1,
        text='Password',
        font=small_font).pack()

    password_str = tk.StringVar()
    password = ttk.Entry(tab1,width=30,textvariable=password_str)
    password.pack(pady=1)

    ttk.Button(tab1,text=button_text,command=append_to_treeview).pack(pady=10)
    
    return tab1
#Password Database
def create_tab2(parent):

    tab2 = ttk.Frame(master = parent)

    global data_table
    data_table = ttk.Treeview(tab2, columns = ('app', 'login','pass'),show='headings')
    data_table.heading('app',text='Apps',anchor='center')
    data_table.heading('login',text='Login',anchor='center')
    data_table.heading('pass',text='Password',anchor='center')
    data_table.pack(expand=True,fill='both')

    return tab2
#Password Generator
def create_tab3(parent):
    
    tab3 = ttk.Frame(master = parent)

    def randomcode_press():
        code_length = entry_letters_int.get()
        code = list(''.join(random.choice("ABCDEFGHIJKLMNOPRSTUWabcdefghijklmnoprstuwz1234567890!@#$%^&*")for i in range(code_length))) 
        random.shuffle(code)

        output_string1.set(code) #type:ignore

    def randomcode(event):
        code_length = entry_letters_int.get()
        code = list(''.join(random.choice("ABCDEFGHIJKLMNOPRSTUWabcdefghijklmnoprstuwz1234567890!@#$%^&*")for i in range(code_length))) 
        random.shuffle(code)

        output_string1.set(code) #type:ignore


    # Title 1

    title_Label1 = tk.Label(tab3, text = "Password Generator", font = big_font)
    title_Label1.pack()

    how_many_Label = tk.Label(tab3, text = 'Enter code length:', font ='Calibri 12')
    how_many_Label.pack()

    # Input Frame 1

    input_frame2 = tk.Frame(tab3)
    input_frame2.pack()


    entry_letters_int = tk.IntVar()
    entry_letters = ttk.Entry(master= input_frame2, textvariable=entry_letters_int)

    entry_letters.bind('<Return>', randomcode)

    entry_letters.focus()
    entry_letters.pack()


    # Button 1 Generate
    button1 = tk.Button(tab3, text = 'Generate',width=10, command = randomcode_press)
    button1.pack(pady=10)

    # Button 1 Copy
    buttonC = tk.Button(tab3, text = 'Copy',width=10, command = lambda: pyperclip.copy(str(output_string1.get())))
    buttonC.pack()

    # Output 1

    output_string1 = tk.StringVar()
    output_Label1 = ttk.Label(tab3, font = 'Calibri 15', textvariable=output_string1)

    output_Label1.pack(pady=5)

    return tab3

# main
window = ttkbootstrap.Window(themename="vapor")
window.geometry('610x400')
window.title("Anrunt's password manager")

# Font 
big_font = Font(
    family='Unispace-Bold',
    size = 32,    
)

small_font = Font(
    family='Times',
    size=10
)

# notebook 
notebook = ttk.Notebook(window)

# widgets
tab1 = create_tab1(notebook,'Password Manager','Confirm')
tab2 = create_tab2(notebook)
tab3 = create_tab3(notebook)


# notebook add + pack
notebook.add(tab1, text='Save Password')
notebook.add(tab2, text='Password Library')
notebook.add(tab3, text='Password Generator')

notebook.pack(expand=True,fill='both')

window.mainloop()

