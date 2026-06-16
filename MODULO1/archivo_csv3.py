import csv

# Crear una lista de datos para escribir en el archivo CSV
datos =[
    ['Portatil', '25000000'],
    ['Celular', '15000000'],
    ['Tablet', '20000000']
]

    # Escribir datos en un archivo CSV
with open('inventario.csv', 'w', newline='', encoding='utf-8') as archivo:
    # csv.writer devuelve un objeto que permite escribir filas en el archivo CSV
    escritor = csv.writer(archivo)  
    #writer.writerow() se utiliza para escribir una fila en el archivo CSV. En este caso, se escribe la fila de encabezados con los nombres de las columnas "Producto" y "Precio"
    escritor.writerow(['Producto', 'Precio'])  # Escribir la fila de encabezados  
    # Escribir las filas de datos
    for fila in datos:
    #writer.writerow() toma una lista como argumento y escribe cada elemento de la lista como una celda en la fila del archivo CSV
        escritor.writerow(fila)