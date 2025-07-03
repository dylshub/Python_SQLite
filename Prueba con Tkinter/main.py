import tkinter as tk
import sqlite3

#BASE Y TABLAS
conexion = sqlite3.connect("colegio.db")
cursor = conexion.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS alumnos(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               nombre TEXT NOT NULL
               )

""")
conexion.commit()
print("BASE DE DATOS Y TABLA CREADA")

#funciones 

def add():
    windowadd = tk.Tk()
    windowadd.title("CRUD MODERNO")
    windowadd.geometry("700x450")
    windowadd.configure(bg=COLOR_FONDO)

    # Frame central
    frame = tk.Frame(windowadd, background=COLOR_FRAME, padx=40, pady=40)
    frame.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.8, relheight=0.8)

    # Etiqueta main
    etiqueta = tk.Label(
    frame,
    text="RELLENE LOS CAMPOS",
    fg=COLOR_TEXTO,
    bg=COLOR_FRAME,
    font=("Segoe UI Semibold", 16)
        )
    etiqueta.place(relx = 0.5, rely=0.05, anchor = "center")

    # Etiqueta de NOMBRE
    lblName = tk.Label(
        frame,
        text="NOMBRE:",
        fg=COLOR_TEXTO,
        bg=COLOR_FRAME,
        font=("Segoe UI Semibold", 16)
    )
    lblName.place(relx = 0.1, rely=0.25)

    #Entrada: nombre
    txtName =tk.Entry(
        frame,
        fg=COLOR_TEXTO,
        font=("Segoe UI Semibold", 14)

    )
    txtName.place(relx = 0.4, rely=0.25)

    # Etiqueta de APELLIDO
    lblLastName = tk.Label(
        frame,
        text="Apellido:",
        fg=COLOR_TEXTO,
        bg=COLOR_FRAME,
        font=("Segoe UI Semibold", 16)
    )
    lblLastName.place(relx = 0.1, rely=0.37)

    #Entrada: Apellido
    txtName =tk.Entry(
        frame,
        fg=COLOR_TEXTO,
        font=("Segoe UI Semibold", 14)

    )
    txtName.place(relx = 0.4, rely=0.37)

    # Etiqueta GRADO
    etiqueta = tk.Label(
        frame,
        text="GRADO: ",
        fg=COLOR_TEXTO,
        bg=COLOR_FRAME,
        font=("Segoe UI Semibold", 16)
        )
    etiqueta.place(relx = 0.5, rely=0.05, anchor = "center")

    #GRADOS
    cuarto = tk.Radiobutton(frame, text = "Cuarto")

    # Botón 1: Guardar
    boton1 = tk.Button(
        frame,
        text="GUARDAR ESTUDIANTE",
        fg=COLOR_TEXTO_BOTON,
        bg=COLOR_BOTON,
        font=FUENTE,
        activebackground="#b47107",
        activeforeground=COLOR_TEXTO_BOTON,
        padx=10,
        pady=10,
        borderwidth=0,
        command = add
    )
    boton1.place(relx = 0.1, rely=0.90)



# Paleta de colores
COLOR_FONDO = "#00225D"
COLOR_FRAME = "#FFFFFF"
COLOR_TEXTO = "#000000"
COLOR_BOTON = "#CC912B"
COLOR_TEXTO_BOTON = "#FFFFFF"

FUENTE = ("Segoe UI", 13)

# Ventana principal
window = tk.Tk()
window.title("CRUD MODERNO")
window.geometry("700x450")
window.configure(bg=COLOR_FONDO)

# Frame central
frame = tk.Frame(window, background=COLOR_FRAME, padx=40, pady=40)
frame.place(relx=0.5, rely=0.5, anchor="center")

# Etiqueta de bienvenida
etiqueta = tk.Label(
    frame,
    text="BIENVENIDO AL SISTEMA DE REGISTRO",
    fg=COLOR_TEXTO,
    bg=COLOR_FRAME,
    font=("Segoe UI Semibold", 16)
)
etiqueta.pack(pady=(0, 25))

# Botón 1: Agregar estudiante
boton1 = tk.Button(
    frame,
    text="➕  AGREGAR ESTUDIANTE",
    fg=COLOR_TEXTO_BOTON,
    bg=COLOR_BOTON,
    font=FUENTE,
    activebackground="#b47107",
    activeforeground=COLOR_TEXTO_BOTON,
    padx=10,
    pady=10,
    borderwidth=0,
    command = add
)
boton1.pack(pady=10, fill="x")

# Botón 2: Ver registros
boton2 = tk.Button(
    frame,
    text="📋  VER REGISTROS",
    fg=COLOR_TEXTO_BOTON,
    bg=COLOR_BOTON,
    font=FUENTE,
    activebackground="#d88807",
    activeforeground=COLOR_TEXTO_BOTON,
    padx=10,
    pady=10,
    borderwidth=0
)
boton2.pack(pady=10, fill="x")

# Botón 3: Salir
boton3 = tk.Button(
    frame,
    text="❌  SALIR",
    fg=COLOR_TEXTO_BOTON,
    bg=COLOR_BOTON,
    font=FUENTE,
    activebackground="#d88807",
    activeforeground=COLOR_TEXTO_BOTON,
    padx=10,
    pady=10,
    borderwidth=0,
    command=window.destroy
)
boton3.pack(pady=10, fill="x")

window.mainloop()
