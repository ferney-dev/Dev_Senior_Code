carro= {
    "marca": "Toyota",
    "modelo": "Corolla",
    "año": 2020,
    "color": "Rojo",
    "colores": ["Rojo", "Blanco", "Negro"],
    "electrico": False
}

print(carro)
print(carro["colores"])
print(type(carro)
      )

"""
===========================================
📚 MÉTODOS DE DICCIONARIOS EN PYTHON
===========================================

Un diccionario en Python es una estructura de datos
que almacena pares clave:valor.

Ejemplo básico:
"""

estudiante = {
    "nombre": "Juan",
    "edad": 20,
    "nota": 4.5
}

# ===========================================
# 1. clear() → Elimina todos los elementos
# ===========================================

copia = estudiante.copy()
copia.clear()
print("clear():", copia)  # {}

# ===========================================
# 2. copy() → Crea una copia del diccionario
# ===========================================

copia = estudiante.copy()
print("copy():", copia)

# ===========================================
# 3. fromkeys() → Crea un diccionario con claves dadas
# ===========================================

claves = ["a", "b", "c"]
nuevo = dict.fromkeys(claves, 0)
print("fromkeys():", nuevo)  # {'a': 0, 'b': 0, 'c': 0}

# ===========================================
# 4. get() → Obtiene valor de una clave
# ===========================================

print("get():", estudiante.get("nombre"))  # Juan
print("get() inexistente:", estudiante.get("direccion", "No existe"))

# ===========================================
# 5. items() → Devuelve pares clave-valor
# ===========================================

print("items():")
for clave, valor in estudiante.items():
    print(clave, valor)

# ===========================================
# 6. keys() → Devuelve todas las claves
# ===========================================

print("keys():", estudiante.keys())

# ===========================================
# 7. values() → Devuelve todos los valores
# ===========================================

print("values():", estudiante.values())

# ===========================================
# 8. pop() → Elimina un elemento por clave
# ===========================================

copia = estudiante.copy()
copia.pop("edad")
print("pop():", copia)

# ===========================================
# 9. popitem() → Elimina el último elemento
# ===========================================

copia = estudiante.copy()
copia.popitem()
print("popitem():", copia)

# ===========================================
# 10. setdefault() → Obtiene valor o lo crea
# ===========================================

copia = estudiante.copy()
valor = copia.setdefault("ciudad", "Armenia")
print("setdefault():", copia)

# ===========================================
# 11. update() → Actualiza el diccionario
# ===========================================

copia = estudiante.copy()
copia.update({"nota": 5.0, "ciudad": "Bogotá"})
print("update():", copia)

"""
===========================================
🧠 RESUMEN IMPORTANTE
===========================================

✔ clear()       → vacía el diccionario
✔ copy()        → crea copia
✔ fromkeys()    → crea nuevo diccionario
✔ get()         → obtiene valor sin error
✔ items()       → clave + valor
✔ keys()        → solo claves
✔ values()      → solo valores
✔ pop()         → elimina por clave
✔ popitem()     → elimina último
✔ setdefault()  → obtiene o crea clave
✔ update()      → actualiza valores

===========================================
💡 CONSEJO PRO
===========================================

Los más usados en proyectos reales son:

- get()
- update()
- items()
- keys()
- values()

===========================================

"""