# Nombramos una variable con el nombre de "archivo".
# Le indicamos que abra un documento con el nombre "demofile.txt".
archivo = open("ALUMNOS.txt", "r")

# Con la función (.readable()) podemos verificar si es leíble o no.
print(archivo.readable())
print(" ")

# Con la función (.readline()) podemos leer la primer línea del documento deseado.
print(archivo.readline())
print(" ")

# Con la función (.read()) podemos leer de manera directa el documento.
print(archivo.read())

# Cerramos el archivo abierto.
archivo.close()

# Escritura de archivos en Python
# Abrimos o creamos el archivo "demofile2.txt" en modo anexar.
archivo_escritura = open("demofile2.txt", "a")
archivo_escritura.write("Ahora el archivo tiene más contenido!\n")
archivo_escritura.close()

# Abrimos y leemos el archivo después de agregar contenido.
archivo_escritura = open("demofile2.txt", "r")
print(archivo_escritura.read())
archivo_escritura.close()

# Abrimos el archivo "demofile3.txt" en modo escribir.
archivo_sobrescribir = open("demofile3.txt", "w")
archivo_sobrescribir.write("¡Ups! He eliminado el contenido anterior.\n")
archivo_sobrescribir.close()

# Abrimos y leemos el archivo después de sobrescribir.
archivo_sobrescribir = open("demofile3.txt", "r")
print(archivo_sobrescribir.read())
archivo_sobrescribir.close()

# Eliminar archivo de Python
import os
# Comprobamos si el archivo "demofile.txt" existe y lo eliminamos.
if os.path.exists("demofile.txt"):
    os.remove("demofile.txt")
    print("El archivo 'demofile.txt' ha sido eliminado.")
else:
    print("El archivo 'demofile.txt' no existe.")

# Eliminar carpeta
# Eliminamos la carpeta "myfolder".
if os.path.exists("myfolder"):
    os.rmdir("myfolder")
    print("La carpeta 'myfolder' ha sido eliminada.")
else:
    print("La carpeta 'myfolder' no existe.")