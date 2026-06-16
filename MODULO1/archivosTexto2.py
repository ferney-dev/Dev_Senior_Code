"""
archivo = open("datos1.txt", "w")
archivo.write("Saludos para todos")
archivo.close()
"""
with open("datos2.txt", "w", encoding="utf-8") as archivo:
    archivo.write("Saludos para todos")

with open("datos2.txt", "r", encoding="utf-8") as archivo:
    linea = archivo.readline()
    print(linea)

with open("datos2.txt", "a", encoding="utf-8") as archivo:
    archivo.write("\nQue onda pues pelaitos")

with open("datos2.txt", "r", encoding="utf-8") as archivo:
    lineas = archivo.readlines()
    print(lineas)
    for x in lineas:
        x = x.rstrip('\n')
        print(x)