# frutas = ("manzana", "pera", "naranja")
# frutas2 = tuple(("sandia", "melon", "kiwi", "cereza", "durazno"))
# print(frutas)
# print(type(frutas))
# print(frutas2)
# print(type(frutas2))

frutas = ("manzana", "pera", "naranja")
print(frutas)

# se usa count() para contar el número de veces que un elemento aparece en la tupla, y index() para encontrar la posición de un elemento específico en la tupla.
print(frutas.count("manzana"))

# se puede acceder a los elementos de la tupla utilizando índices, al igual que con las listas, pero no se pueden modificar los elementos de una tupla después de su creación.
print(frutas.index("naranja"))