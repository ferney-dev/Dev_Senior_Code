# lista es una estructura de datos que permite almacenar una colección de elementos ordenados y mutables.

#-------------------------------------------------------------
# a = [1, 2, 3, 4, 5, "mama", True, 3.14, [6,7,8]]
# print(a)
# print(a[0])
# print(a[5])
# print(a[8][2])


#-------------------------------------------------------------
# a = ["fresa", "manzana", "pera", "naranja", "uva", "sandia", "melon", "kiwi", "cereza", "durazno"]
# print(len(a[4]))

#a = ["fresa", "manzana", "pera", "naranja", "uva"]
# suma = 0
# for elemento in a:
#     suma += len(elemento)
# print(suma)

#-------------------------------------------------------------
# a = ["fresa", "manzana", "pera", "naranja", "uva"]
# b = list(("sandia", "melon", "kiwi", "cereza", "durazno"))
# print(a)
# print(type(a))
# print(b)
# print(type(b))

#-------------------------------------------------------------
# a = ["fresa", "manzana", "pera", "naranja", "uva"]

# numero= 0
# while numero< len(a):
#     print(a[numero])
#     numero+= 1

# a = ["fresa", "manzana", "pera", "naranja", "uva"]
# # se puede eliminar un elemento de la lista utilizando el método remove() o pop()
# a.clear(a)

# # se puede eliminar toda la lista utilizando la función del()
# del a
# print(a)

# # se usa copy() para crear una copia de la lista original, lo que permite modificar la copia sin afectar a la lista original.
# a.copy()
# print(a)

# # se puede contar el número de veces que un elemento aparece en la lista utilizando el método count()
# a.count("fresa")
# print(a)

# # se puede agregar un elemento al final de la lista utilizando el método append()
# a.extend(["sandia", "melon", "kiwi", "cereza", "durazno"])
# print(a)

# # se puede insertar un elemento en una posición específica utilizando el método insert()
# a = ["fresa", "manzana", "pera", "naranja", "uva"]
# print(a.index("naranja"))

# # se usa insert() para insertar un elemento en una posición específica de la lista, desplazando los elementos existentes hacia la derecha.
# a.insert(3, "sandia")
# print(a)

# # se usa pop para eliminar un elemento de la lista en una posición específica y devolverlo. Si no se especifica un índice, pop() eliminará y devolverá el último elemento de la lista.
# a.pop(3)
# print(a)

# #se usa sort() para ordenar los elementos de la lista en orden ascendente. Si se desea ordenar en orden descendente, se puede usar el argumento reverse=True.
# a.sort()
# print(a)

# # se usa reverse() para invertir el orden de los elementos en la lista.
# a.reverse()
# print(a)

"""pedir al usaurio que ingrese notas entre 0 y 10nhasta que ingrese -1
para finalizar luego mostrar el promedio de las notas ingresadas"""

"""
pedir al usuario que ingrese notas entre 0 y 10, 
hasta que ingrese -1 para finalizar. 
Luego, mostrar el promedio de las notas ingresadas.
"""
notas = []
while True:    
    nota = float(input("Ingrese una nota entre 0 y 10 (o -1 para finalizar): "))
    if nota == -1:
        break
    if 0 <= nota <= 10:
        notas.append(nota)
    else:
        print("Nota inválida. Por favor, ingrese una nota entre 0 y 10.")

if notas:
    promedio = sum(notas) / len(notas)
    print(f"El promedio de las notas ingresadas es: {promedio}")
else:
    print("No se ingresaron notas válidas.")

