import csv

# Escribir datos en un archivo CSV
with open('usuarios.csv', 'w', newline='',encoding='utf-8') as archivo:
    # Crear un objeto escritor de CSV
    campos = ['Nombre', 'Edad', ]
    # Crear un objeto escritor de CSV
    escritor = csv.DictWriter(archivo, fieldnames=campos)
    # Escribir el encabezado
    escritor.writeheader()
    
    escritor.writerow({'Nombre': 'Juan', 'Edad': 30})
    escritor.writerow({'Nombre': 'María', 'Edad': 25})