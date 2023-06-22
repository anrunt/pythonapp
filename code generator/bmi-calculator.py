import tkinter as tk
from tkinter import ttk
from math import pow
import customtkinter as ctk
from PIL import Image,ImageTk



def get_result():

        result = float(kg_entry_str.get()) / pow((float(m_entry_str.get())),2)
        rounded_result = round(result,2) 
        output_label_str.set(float((rounded_result)))
        

        #GIGACHAD
        
        if rounded_result >= 18 and rounded_result <= 25:

            wynik_str.set('Gicyk')
            
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

            # Importing gigachad image
            image_original = Image.open('gigachad2.jpg')
            image_ratio = image_original.size[0] / image_original.size[1]
            image_tk = ImageTk.PhotoImage(image_original)

            # Canvas image
            canvas = tk.Canvas(extra_window, background='black', bd = 0, highlightthickness = 0, relief = 'ridge')
            canvas.grid(column = 0, columnspan = 4, row = 0, sticky = 'nsew')

            canvas.bind('<Configure>', show_full_image)




        # SZKIELET

        elif rounded_result <= 16:
            wynik_str.set('Wygłodzony szkielecik') 

            def show_full_image(event):
                global resized_tk

                # Current ratio
                canvas_ratio = event.width / event.height

                # Get coordinates
                if canvas_ratio > image_ratio_skeleton:
                    height = int(event.height)
                    width = int(height* image_ratio_skeleton)
                else:
                    width = int(event.width)
                    height = int(width / image_ratio_skeleton)
                
                resized_image = image_skeleton_original.resize((width,height))
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

            
            #Importing skeleton image 
            image_skeleton_original = Image.open('szkielecik.jpg')
            image_ratio_skeleton = image_skeleton_original.size[0] / image_skeleton_original.size[1]
            image_skeleton_tk = ImageTk.PhotoImage(image_skeleton_original)


            # Canvas image
            canvas = tk.Canvas(extra_window, background='black', bd = 0, highlightthickness = 0, relief = 'ridge')
            canvas.grid(column = 0, columnspan = 4, row = 0, sticky = 'nsew')

            canvas.bind('<Configure>', show_full_image)


        # GRUBAS

        elif rounded_result >=35:
            wynik_str.set('Ale grubas')
            
            def show_full_image(event):
                global resized_tk

                # Current ratio
                canvas_ratio = event.width / event.height

                # Get coordinates
                if canvas_ratio > image_ratio_grubas:
                    height = int(event.height)
                    width = int(height* image_ratio_grubas)
                else:
                    width = int(event.width)
                    height = int(width / image_ratio_grubas)
                
                resized_image = image_grubas_original.resize((width,height))
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

            
            #Importing skeleton image 
            image_grubas_original = Image.open('grubas.jpg')
            image_ratio_grubas = image_grubas_original.size[0] / image_grubas_original.size[1]
            image_grubas_tk = ImageTk.PhotoImage(image_grubas_original)


            # Canvas image
            canvas = tk.Canvas(extra_window, background='black', bd = 0, highlightthickness = 0, relief = 'ridge')
            canvas.grid(column = 0, columnspan = 4, row = 0, sticky = 'nsew')

            canvas.bind('<Configure>', show_full_image)

    
        
# Setup 
window = ctk.CTk()
window.geometry('400x265')
window.title('BMI CALCULATOR')
window.resizable(False,False)

# Canvas 
canvas = tk.Canvas(window,width=400, height=300, background='black',bd=0, highlightthickness=0, relief='ridge')
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
    bg_color='black',
    border_color='black',
    corner_radius=10)

m_entry = ctk.CTkEntry(
    window,
    width = 100,
    textvariable = m_entry_str,
    fg_color='green',
    text_color='yellow',
    bg_color='black',
    border_color='black',
    corner_radius=10)

button = ctk.CTkButton(
    window,
    corner_radius=10,
    text='Calculate',
    fg_color = 'green',
    text_color = 'yellow',
    hover_color= 'blue',
    bg_color='black',
    border_color='black',
    width=100,
    command = get_result)

output_label_str = ctk.StringVar()
output_label =ctk.CTkLabel(
    window,
    font = ('Arial', 18),
    width = 100,
    fg_color='black',
    text_color='yellow',
    textvariable = output_label_str)

wynik_str = ctk.StringVar()
wynik = ctk.CTkLabel(
    window,
    font = ('Arial',18),
    width=150,
    fg_color='black',
    text_color='yellow',
    textvariable = wynik_str
)       


kg_entry_window = canvas.create_window((190,90),window = kg_entry)
m_entry_window = canvas.create_window((190,150),window = m_entry)
output_label_window = canvas.create_window((190,180), window=output_label)
button_window = canvas.create_window((190,210),window=button)
wynik_window = canvas.create_window((190,240),window = wynik)

# Run 
window.mainloop()