import tkinter as tk
from tkinter import Tk, ttk, Label, Text, Listbox, Button, END, StringVar
from tkinter.filedialog import askdirectory, askopenfilename
from pdf import creation

def get_file_path():
    filename = askopenfilename()
    ph.delete("1.0", END)
    ph.insert(END, filename)
    ph.update()

def get_dir_path():
    filename = askdirectory()
    ph_dir.delete("1.0", END)
    ph_dir.insert(END, filename)
    ph_dir.update()

def pdf_creation():
    file_ph = ph.get("1.0", END).replace('\n', "")
    dir_path = ph_dir.get("1.0", END).replace('\n', "")
    creation(file_ph, dir_path)

root = Tk()

root.title("IEB Currículos")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

app_height = 250
app_width = 350

x_coord = int((screen_width/2) - (app_width/2))
y_coord = int((screen_height/2) - (app_height/2))

root.geometry("{}x{}+{}+{}".format(app_width, app_height, x_coord, y_coord))
root.configure(background='#4BA88C')

title = Label(root, text="IEB Curriculos", font=("Times New Roman", 20), bg='#4BA88C', foreground='#000000')
title.grid(row=0, column=1, columnspan=3, pady=5)

path_description = Label(root, text="Escolha o arquivo de dados", font=("Times New Roman", 14), foreground='#000000', bg='#4BA88C')
path_description.grid(row=1,column=1, columnspan=3, pady=5)

ph = Text(root, height=1, width=35, borderwidth=0)
ph.grid(row=2, column=1, columnspan=2, padx=5)

file_path = Button(root, text="C:/", command=get_file_path, background='#4BA88C', borderwidth=0)
file_path.grid(row=2, column=3, pady=5)    

path_dir_description = Label(root, text="Escolha o repositório para os currículos", font=("Times New Roman", 14), foreground='#000000', bg='#4BA88C')
path_dir_description.grid(row=3,column=1, columnspan=3, pady=5)

ph_dir = Text(root, height=1, width=35, borderwidth=0)
ph_dir.grid(row=4, column=1, columnspan=2, padx=5)

file_path_dir = Button(root, text="C:/", command=get_dir_path, background='#4BA88C', borderwidth=0)
file_path_dir.grid(row=4, column=3, pady=5)

button2 = Button(root, text="Gerar PDF", command=pdf_creation, background='#4BA88C', borderwidth=0)
button2.grid(row=5, column=1, columnspan=3, pady=10)

text_var = StringVar(root)

root.mainloop()