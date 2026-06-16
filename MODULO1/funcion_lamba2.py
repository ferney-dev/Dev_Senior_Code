"""
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)

def pares(paqueticodemani):
    resultado = []
    for numero in paqueticodemani:
        if numero % 2 == 0:
            resultado.append(numero)
    return resultado

numeros_pares = pares(numeros)
print(numeros_pares)
"""