import csv

# Escribir datos en un archivo CSV
with open('estudiante.csv','w', encoding="utf-8") as archivo:
    # csv.writer devuelve un objeto que permite escribir filas en el archivo CSV
    writer = csv.writer(archivo)
    # Escribir la fila de encabezados y las filas de datos
    writer.writerow(['Nombre', 'Edad', 'Grado'])
    writer.writerow(['Juan', 20, 'A'])
    writer.writerow(['María', 22, 'B'])
    writer.writerow(['Pedro', 19, 'A'])