from conexion import crear_bd
from interfaz import interfaz
from funcionalidades import agregar_categoria, agregar_plato, mostrar_menu, menu

crear_bd()

while True:
    print("--------¡Bienvenido al sistema de edicion del menu!--------")
    menu()
    seleccion = input("Introduce una de las opciones del menú: ")
    match seleccion:
        case "1":
            print("--------Nueva Categoria-------")
            agregar_categoria()
        case "2":
            print("--------Nuevo Plato--------")
            agregar_plato()
        case "3":
            print("--------Menu--------")
            mostrar_menu()
        case "4":
            interfaz()
        case "5":
            print("Hasta Luego")
            break
        case _:
            print("Opcion no disponible")
