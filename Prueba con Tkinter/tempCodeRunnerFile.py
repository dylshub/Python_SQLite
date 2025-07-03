import tkinter as tk

# Paleta de colores
COLOR_FONDO = "#00225D"
COLOR_FRAME = "#FFFFFF"
COLOR_TEXTO = "#000000"
COLOR_BOTON = "#F29D0B"
COLOR_TEXTO_BOTON = "#6E6E64FF"

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
    text="🎓 BIENVENIDO AL SISTEMA DE REGISTRO",
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
    activebackground="#d88807",
    activeforeground=COLOR_TEXTO_BOTON,
    padx=10,
    pady=10,
    borderwidth=0
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
