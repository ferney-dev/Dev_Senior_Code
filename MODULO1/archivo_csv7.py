import csv

with open("malo.csv","r",encoding="utf-8") as f:
    lector = csv.DictReader(f)
    for fila in lector:
        try:
            nombre = fila["nombre"]
            precio = float(fila["precio"])
            cantidad = int(fila["cantidad"])
            if precio < 0 or cantidad < 0:
                print("Valores negativos invalidos")
                continue
            print(nombre,precio,cantidad)
        except (ValueError, TypeError):
            print("Error de formato en la fila:",fila)
        except KeyError:
            print("Falta una columns en la fila:",fila)
            
  
           
