from functools import reduce

numeros = [1, 2, 3, 4, 5]

suma_total = reduce(lambda acumulador, numero: acumulador + numero, numeros)
producto = reduce(lambda acumulador, numero: acumulador * numero, numeros)

print("La suma total es:", suma_total)
print("El producto es:", producto)