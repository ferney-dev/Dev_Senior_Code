# frutas = {"manzana", "banana", "naranja", "pera", "uva"}
# print(len(frutas))

# #se puede agregar un elemento a un conjunto utilizando el método add()
# frutas.add("kiwi")
# print(frutas)

# # se puede eliminar un elemento de un conjunto utilizando el método remove() o discard()
# frutas.remove("banana")
# print(frutas)

# # se usa pop para eliminar un elemento aleatorio del conjunto y devolverlo. Si el conjunto está vacío, se genera una excepción KeyError.
# frutas.pop()
# print(frutas)

# # se usa clear para eliminar todos los elementos del conjunto, dejando un conjunto vacío.
# frutas.clear()
# print(frutas)

# # se usa copy() para crear una copia del conjunto original, lo que permite modificar la copia sin afectar al conjunto original.
# frutas2 = frutas.copy()
# print(frutas2)
# frutas.copy()
# print(frutas)


# se puede contar el número de veces que un elemento aparece en el conjunto utilizando el método count()
frutas1 = {"manzana", "banana", "naranja", "pera", "uva"}
frutas2 = {"kiwi", "sandia", "melon", "cereza", "durazno"}
print(frutas1.difference(frutas2))# muestra los elementos que están en frutas1 pero no en frutas2

print(frutas1.intersection(frutas2))# muestra los elementos que están en ambos conjuntos

print(frutas1.union(frutas2))# muestra todos los elementos de ambos conjuntos, sin duplicados

frutas1.discard("banana")# elimina el elemento "banana" del conjunto frutas1, si existe. Si el elemento no existe, no se genera un error.
print(frutas1)

frutas1.remove("naranja")# elimina el elemento "naranja" del conjunto frutas1. Si el elemento no existe, se genera un error KeyError.
print(frutas1)

print(frutas1.issubset(frutas2))# devuelve True si todos los elementos de frutas1 están en frutas2, de lo contrario devuelve False.

frutas1.difference_update(frutas2)# elimina los elementos de frutas1 que también están en frutas2, modificando el conjunto frutas1.
print(frutas1)