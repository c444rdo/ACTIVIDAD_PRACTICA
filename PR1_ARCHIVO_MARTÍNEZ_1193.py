# Nombramos una variable con el nombre de "archivos".
# Le indicamos que abra un documento con el nombre "alumnos.txt".
archivo = open("ALUMNOS.txt", "r")

# Con la función (.readable()) podemos verificar si es leíble o no.
print (archivo.readable())
print (" ")

# Con la función (.readline()) podemos leer la primer linea el documento deseado.
print (archivo.readline())
print (" ")

# Con la función (.read()) podemos leer de manera directa el documento.
print (archivo.read())

# Cerramos el archivo abierto.
archivo.close()