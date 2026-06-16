import csv

# Escribir datos en un archivo CSV
with open('inventario.csv', 'r', encoding='utf-8', newline='') as archivo:
    # Crear un objeto escritor de CSV
    lector = csv.DictReader(archivo)
    # Escribir el encabezado
    for fila in lector:
        # Imprimir los datos de cada fila
        print(fila)