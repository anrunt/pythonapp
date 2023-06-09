import tkinter as tk
import ttkbootstrap as ttk


# Window

window = tk.Tk()
window.geometry('400x300')
window.title("Notebook")

# Notebook widget 

notebook = ttk.Notebook(window)

tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)
notebook.add(tab1, tex= 'tab1')
notebook.add(tab2, tex = 'tab2')

notebook.pack()



# Run
window.mainloop()