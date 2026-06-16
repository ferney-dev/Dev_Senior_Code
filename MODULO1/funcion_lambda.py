
# PROGRAMACION FUNCIONALES

# # Función normal
# def suma4(n1, n2):
#     resultado = n1 + n2
#     return resultado

# # Función lambda
# suma5 = lambda n1, n2: n1 + n2

# print("aca arranca el programa")

# # Llamamos la función y mostramos el resultado
# print(suma4(5,10))

# # Llamamos la función lambda
# print(suma5(5,10))



# # map se usa para recorrer una lista
# # y aplicar una función a cada elemento automáticamente
# numeros = [1,2,3,4,5]

# # lambda x: x * 2
# # toma cada número y lo multiplica por 2

# # map aplica esa operación
# # a todos los elementos de la lista

# dobles = list(map(lambda x: x * 2, numeros))

# # Mostramos la nueva lista
# print(dobles)



nombres = ["Alice","Bob","Charly"]
nombre_mayusculas = list(map( lambda x: x.upper(),nombres))
print(nombre_mayusculas)