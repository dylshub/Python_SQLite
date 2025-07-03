import sqlite3

#Crea o abre un archivo de base de datos (db)
conexion = sqlite3.connect("colegio.db") 

#Crear un cursor para ejecutar comandos sql
cursor = conexion.cursor()

#CREAR UNA TABLA
cursor.execute("""
CREATE TABLE IF NOT EXISTS alumnos(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               nombre TEXT NOT NULL,
               apellido TEXT NOT NULL,
               correo TEXT NOT NULL,
               carrera TEXT NOT NULL,
               grado TEXT NOT NULL,
               domicilio TEXT NOT NULL
               )
""")

#GUARDAR LOS CAMBIOS CERRAR 

conexion.commit()
#conexion.close()

print("BASE DE DATOS Y TABLA CREADA CORRECTAMENTE")

###############################################################

#INSERTAR DATOS 

print("BIENVENIDO")
nombreIngresado = input("Ingrese su nombre ")
apellidoIngresado = input("Ingrese su apellido ")
correoIngresado = input("Ingrese su correo ")
carreraIngresada = input("Ingrese su carrera ")
gradoIngresado = input("Ingrese su grado ")
domicilioIngresado = input("Ingrese su domicilio ")

cursor.execute("INSERT INTO alumnos (nombre, apellido, correo, carrera, grado, domicilio) VALUES (?, ?, ?, ?, ?, ?)", (nombreIngresado, apellidoIngresado, correoIngresado, carreraIngresada, gradoIngresado, domicilioIngresado) )

conexion.commit()
print("USUARIO REGISTRADO CON EXITO")

#MOSTRAR DATOS
alumnos= cursor.execute(" SELECT * FROM alumnos ")
print("____________________________________________________")
print("USUARIOS REGISTRADOS")
for alumnos in alumnos:
    print(alumnos)


#ACTUALIZAR DATOS
print("__________________________________________________")
IdActualizar=input("Ingrese el ID del alumno que desea actualizar")
nombreIngresado = input("Ingrese su nombre ")
apellidoIngresado = input("Ingrese su apellido ")
correoIngresado = input("Ingrese su correo ")
carreraIngresada = input("Ingrese su carrera ")
gradoIngresado = input("Ingrese su grado ")
domicilioIngresado = input("Ingrese su domicilio ")
cursor.execute("""
    UPDATE alumnos 
    SET nombre = ?, apellido = ?, correo = ?, carrera = ?, grado = ?, domicilio = ?
    WHERE id = ?
""", (nombreIngresado, apellidoIngresado, correoIngresado, carreraIngresada, gradoIngresado, domicilioIngresado, IdActualizar))


#ELIMINAR USUARIO
print("___________________________________________________")
IdEliminar = input("ESCRIBA UN ID A ELIMINAR")
cursor.execute("DELETE FROM alumnos WHERE id = ?",IdEliminar)
alumnos= cursor.execute(" SELECT * FROM alumnos ")
print("Alumno eliminado ")
print("_______________________________")
for alumnos in alumnos:
    print(alumnos)

print("USUARIOS ACTUALIZADOS")
conexion.close()
