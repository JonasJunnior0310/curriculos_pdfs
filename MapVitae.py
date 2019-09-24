import tkinter as tk
from tkinter import filedialog, END
from pdf import creation

def get_file_path():
    filename = filedialog.askopenfilename()
    ph.delete("1.0", END)
    ph.insert(END, filename)
    ph.update()

def get_dir_path():
    filename = filedialog.askdirectory()
    ph_dir.delete("1.0", END)
    ph_dir.insert(END, filename)
    ph_dir.update()

def pdf_creation():
    text_var.set("Gerando currículos...")
    file_ph = ph.get("1.0", END).replace('\n', "")
    dir_path = ph_dir.get("1.0", END).replace('\n', "")
    creation(file_ph, dir_path)
    text_var.set("Currículos gerados!")

root = tk.Tk()

root.title("Map Trabalho Currículos")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

app_height = 260
app_width = 330

x_coord = int((screen_width/2) - (app_width/2))
y_coord = int((screen_height/2) - (app_height/2))

root.geometry("{}x{}+{}+{}".format(app_width, app_height, x_coord, y_coord))
root.configure(background='#4BA88C')

title = tk.Label(root, text="Map Trabalho Currículos", font=("Times New Roman", 20), bg='#4BA88C', foreground='#000000')
title.grid(row=0, column=1, columnspan=3, pady=5)

path_description = tk.Label(root, text="Escolha o arquivo de dados", font=("Times New Roman", 14), foreground='#000000', bg='#4BA88C')
path_description.grid(row=1,column=1, columnspan=3, pady=5)

ph = tk.Text(root, height=1, width=35, borderwidth=1)
ph.grid(row=2, column=1, columnspan=2, padx=5)

file_path = tk.Button(root, text="C:/", command=get_file_path, background='#4BA88C', borderwidth=1)
file_path.grid(row=2, column=3, pady=5)    

path_dir_description = tk.Label(root, text="Escolha o repositório para os currículos", font=("Times New Roman", 14), foreground='#000000', bg='#4BA88C')
path_dir_description.grid(row=3,column=1, columnspan=3, pady=5)

ph_dir = tk.Text(root, height=1, width=35, borderwidth=1)
ph_dir.grid(row=4, column=1, columnspan=2, padx=5)

file_path_dir = tk.Button(root, text="C:/", command=get_dir_path, background='#4BA88C', borderwidth=1)
file_path_dir.grid(row=4, column=3, pady=5)

button2 = tk.Button(root, text="Gerar PDF", command=pdf_creation, background='#4BA88C', borderwidth=1)
button2.grid(row=5, column=1, columnspan=3, pady=10)

text_var = tk.StringVar(root)

process_monitor = tk.Label(root, textvariable=text_var, bg='#4BA88C')
process_monitor.grid(row=6, column=1, columnspan=3, pady=5)


root.mainloop()