import csv

# Leer datos de un archivo CSV
with open('inventario.csv', 'r',  newline='', encoding='utf-8') as archivo:
    # Crear un objeto lector de CSV
    lector = csv.DictReader(archivo)
    # Imprimir los datos de cada fila
    for fila in lector:
    # Imprimir el producto y su precio
        print(fila['Producto'], fila['Precio'])


