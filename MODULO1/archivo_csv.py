import csv

# Leer datos de un archivo CSV
with open('productos.csv', 'r', encoding='utf-8') as archivo:
    # csv.reader devuelve un iterador que recorre cada fila del archivo CSV
    lector_csv = csv.reader(archivo)
    # Si el archivo CSV tiene encabezados, puedes saltar la primera fila  
    next(lector_csv) 
    # Iterar sobre cada fila del archivo CSV
    for fila in lector_csv:
        nombre = fila[0]
        precio = float(fila[1])
        cantidad = int(fila[2])
        print(f'Producto: {nombre}, Precio: {precio}, Cantidad: {cantidad}')
    