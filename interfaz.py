import sqlite3
from tkinter import *

def interfaz():
    root = Tk()
    root.title("Menú")
    root.config(bd=35, relief='sunken')

    label = Label(root, text="Menú del día", fg="deeppink", font=("Helvetica, 25"))
    label.pack()
    label = Label(root, text= '')
    label.pack()

    conexion = sqlite3.connect('menu.db')
    cursor = conexion.cursor()
    categorias = cursor.execute("SELECT * from categorias").fetchall()
    for c in categorias:
        label = Label(root, text= "{}".format(c[1]), fg="purple", font=("Helvetica, 21"))
        label.pack()
        platos = cursor.execute("SELECT * from platos WHERE categoria_id={}".format(c[0])).fetchall()
        for p in platos:
            label = Label(root, text= "{}".format(p[1]), fg="black", font=("Helvetica, 18"))
            label.pack()

    label = Label(root, text= '')
    label.pack()
    label = Label(root, text="12€ (Iva Incluido)", fg="maroon", font=("Helvetica, 15"))
    label.pack()
    conexion.close()

    root.mainloop()
