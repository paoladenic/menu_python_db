import sqlite3

def agregar_categoria():
    nombre = input("Introduce el nombre de la categoría: ")
    nombre_categoria = nombre.title()
    conexion = sqlite3.connect('menu.db')
    cursor = conexion.cursor()
    try:
        cursor.execute("INSERT INTO categorias VALUES (null, '{}')".format(nombre_categoria))
    except sqlite3.IntegrityError:
        print("La categoría ya existe.")
    else:
        print("Categoría agregada correctamente.")         
    conexion.commit()
    conexion.close()


def agregar_plato():
    conexion = sqlite3.connect("menu.db")
    cursor = conexion.cursor()
    categorias = cursor.execute("SELECT * from categorias").fetchall()
    print("Escoje una categoria a la que le quieres agregar un plato: ")
    for c in categorias:
        print("[{}] {}".format(c[0], c[1]))
    categoria_usuario = int(input('> '))
    mayus = input("Ingresa el nombre del plato que quieres añadir a la categoria escogida: ")
    plato = mayus.capitalize()
    try:
        cursor.execute("INSERT INTO platos VALUES (null, '{}', {})".format(plato, categoria_usuario))
    except sqlite3.IntegrityError:
        print("El plato ya existe.")
    else:
        print("Plato {} agregado correctamente.".format(plato))         
    conexion.commit()
    conexion.close()


def mostrar_menu():
    conexion = sqlite3.connect("menu.db")
    cursor = conexion.cursor()
    categorias = cursor.execute("SELECT * from categorias").fetchall()
    for c in categorias:
        print(c[1])
        platos = cursor.execute("SELECT * from platos WHERE categoria_id={}".format(c[0])).fetchall()
        for p in platos:
            print('\t{}'.format(p[1]))
    conexion.commit()
    conexion.close()


def menu():
            print("""
                    1.- Crear una nueva categoria \n
                    2.- Crear un nuevo plato \n
                    3.- Mostrar el menu \n
                    4.- Genera tu menu digital \n  
                    5.- Salir \n
                    """)
            