#Archivos .txt # texto
#Archivos .csv # valores separados por comas
#Archivos .json # formato de intercambio de datos


# r: read para leer, w: write para escribir,
# a: append para agregar al final, r+ para leer y escribir
# x para crear un nuevo archivo, si el archivo ya existe, genera un error
archivo = open("tareas.txt", "w") # Abrir el archivo en modo lectura
archivo.write("Tarea 1: Hacer la compra\n")# Escribir en el archivo, si el archivo no existe, lo crea
archivo.close() # Cerrar el archivo después de usarlo


archivo = open("tareas.txt", "r") # Abrir el archivo en modo lectura
linea = archivo.readline() # Leer una línea del archivo
print(linea) # Imprimir la línea leída
archivo.close() # Cerrar el archivo después de usarlo

archivo = open("tareas.txt", "r") # Abrir el archivo en modo append para agregar al final
lineas = archivo.readlines() # Leer todas las líneas del archivo
print(lineas) # Imprimir las líneas leídas
archivo.close() # Cerrar el archivo después de usarlo
for linea in lineas: # Iterar sobre las líneas leídas
    linea = linea.rstrip() # Eliminar los espacios en blanco al final de la línea
    print(linea) # Imprimir la línea sin espacios en blanco al final