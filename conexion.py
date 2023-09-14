import sqlite3

def crear_bd():
    try:
        conexion = sqlite3.connect('menu.db')
        cursor = conexion.cursor()
        
        cursor.execute('''CREATE TABLE IF NOT EXISTS categorias (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            nombre TEXT UNIQUE
                        )''')
        
        cursor.execute('''CREATE TABLE IF NOT EXISTS platos (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            nombre TEXT,
                            categoria_id INTEGER,
                            FOREIGN KEY (categoria_id) REFERENCES categorias(id)
                        )''')
        
        conexion.commit()
        conexion.close()
        print("La(s) tabla(s) se ha(n) creado corectamente!!")
    except sqlite3.OperationalError:
        print("Las tablas ya existen!!!")