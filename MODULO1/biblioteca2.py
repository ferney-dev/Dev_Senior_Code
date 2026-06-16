"""

Sistema de Gestión de Biblioteca
🎯 Objetivo del reto

Diseñar la estructura de datos más adecuada para representar una biblioteca utilizando listas, 
diccionarios, conjuntos y tuplas.

El reto no consiste únicamente en almacenar datos, sino en pensar como un arquitecto de software,
seleccionando la estructura correcta para cada tipo de información.

📚 Contexto

Una biblioteca necesita almacenar información sobre:

Libros
Autores
Usuarios
Préstamos
Fechas
Categorías

Tu equipo debe diseñar un modelo de datos que permita representar toda esta información
de forma organizada y sin redundancias.

📝 Requerimientos del sistema
1. Libros

Cada libro debe almacenar:

ISBN
Título
Año de publicación
Lista de autores
Categorías
Número total de copias
Número de copias disponibles

2. Autores

Cada autor debe tener:

Identificación única
Nombre
Nacionalidad
Año de nacimiento

3. Usuarios

Cada usuario debe almacenar:
ID
Nombre completo
Correo electrónico
Teléfono

4. Préstamos

Cada préstamo debe registrar:

ID del préstamo
Usuario
ISBN del libro
Fecha de préstamo
Fecha de devolución
Estado (activo, devuelto, atrasado)

5. Fechas

Las fechas deben almacenarse usando una estructura apropiada.

6. Categorías

No deben existir categorías repetidas.

🎯 Parte 1 — Diseñar el esquema de datos

Construyan una estructura principal llamada biblioteca que contenga toda la información.

Sugerencia:
biblioteca = {
    "autores": {},
    "libros": {},
    "usuarios": {},
    "prestamos": {}
}
🎯 Parte 2 — Cargar datos de ejemplo

Agregar al menos:

3 autores
5 libros
4 usuarios
3 préstamos

🎯 Parte 3 — Consultas a resolver

El programa debe mostrar:

Todos los libros disponibles.
Todos los libros de un autor específico.
Todos los préstamos activos.
Usuarios con préstamos atrasados.
Categorías existentes.
Libro más prestado.
Cantidad total de libros.
Cantidad total de préstamos activos.

🎯 Parte 4 — Justificación técnica

El equipo debe explicar:

¿Por qué usaron diccionarios para ciertas entidades?
¿Por qué las categorías son conjuntos?
¿Por qué las fechas pueden representarse como tuplas?
¿Qué ventajas tiene evitar redundancia?

🎯 Parte 5 — Refactorización

Analicen el siguiente diseño deficiente:

biblioteca = [
    ["978001", "Python Básico", "Juan Pérez", "Programación"],
    ["978002", "Python Avanzado", "Juan Pérez", "Programación"],
    ["978003", "Bases de Datos", "Ana Gómez", "Tecnología"]
]
Preguntas
¿Qué redundancias existen?
¿Qué problemas tendría este diseño?
¿Cómo lo reestructurarían?
🏅 Bonus

Agregar:

Historial de préstamos por usuario.
Búsqueda por categoría.
Ranking de usuarios con más préstamos.
"""

# =========================================
# SISTEMA DE BIBLIOTECA
# =========================================


# =========================================
# DICCIONARIO PRINCIPAL
# Aquí se guarda toda la información
# =========================================

biblioteca = {

    # Guardar autores
    "autores": {

        # ID del autor
        1: {
            "nombre": "Gabriel Garcia Marquez",
            "nacionalidad": "Colombiano",
            "nacimiento": 1927
        },

        2: {
            "nombre": "Julio Verne",
            "nacionalidad": "Frances",
            "nacimiento": 1828
        }

    },


    # Guardar libros
    "libros": {

        # ISBN del libro
        "978001": {

            # Nombre del libro
            "titulo": "Cien años de soledad",

            # Año publicación
            "anio": 1967,

            # Lista de autores
            "autores": [1],

            # Conjunto para no repetir categorías
            "categorias": {"Novela", "Literatura"},

            # Total copias
            "copias": 10,

            # Copias disponibles
            "disponibles": 7
        },

        "978002": {
            "titulo": "Viaje al centro de la tierra",
            "anio": 1864,
            "autores": [2],
            "categorias": {"Aventura", "Ciencia"},
            "copias": 5,
            "disponibles": 2
        }

    },


    # Guardar usuarios
    "usuarios": {

        1: {
            "nombre": "Carlos Lopez",
            "correo": "carlos@gmail.com",
            "telefono": "3001234567"
        },

        2: {
            "nombre": "Ana Torres",
            "correo": "ana@gmail.com",
            "telefono": "3119876543"
        }

    },


    # Guardar préstamos
    "prestamos": {

        1: {

            # Usuario que pidió el libro
            "usuario": 1,

            # Libro prestado
            "isbn": "978001",

            # Fecha usando tupla
            "fecha_prestamo": (2026, 5, 1),

            "fecha_devolucion": (2026, 5, 15),

            # Estado del préstamo
            "estado": "activo"
        }

    }

}


# =========================================
# MOSTRAR LIBROS DISPONIBLES
# =========================================

print("LIBROS DISPONIBLES")

for isbn, libro in biblioteca["libros"].items():

    # Si hay libros disponibles
    if libro["disponibles"] > 0:

        print(libro["titulo"])


# =========================================
# MOSTRAR CATEGORÍAS
# =========================================

print("\nCATEGORIAS")

# Crear conjunto vacío
categorias = set()

# Recorrer libros
for libro in biblioteca["libros"].values():

    # Agregar categorías
    categorias.update(libro["categorias"])

# Mostrar categorías
print(categorias)


# =========================================
# MOSTRAR PRÉSTAMOS ACTIVOS
# =========================================

print("\nPRESTAMOS ACTIVOS")

for prestamo in biblioteca["prestamos"].values():

    # Verificar estado
    if prestamo["estado"] == "activo":

        print(prestamo)