# =========================================
# CREACIÓN DEL DICCIONARIO PRINCIPAL
# =========================================

# Aquí se crea la biblioteca principal.
# Dentro tendrá:
# autores
# libros
# usuarios
# prestamos

biblioteca = {
    "autores": {},
    "libros": {},
    "usuarios": {},
    "prestamos": {}
}

# =========================================
# AUTORES
# =========================================

# Aquí guardamos los autores.
# Cada autor tiene:
# nombre
# nacionalidad
# año de nacimiento

biblioteca["autores"] = {

    # Autor con ID 1
    1: {
        "nombre": "Gabriel García Márquez",
        "nacionalidad": "Colombiana",
        "nacimiento": 1927
    },

    # Autor con ID 2
    2: {
        "nombre": "J.K. Rowling",
        "nacionalidad": "Británica",
        "nacimiento": 1965
    },

    # Autor con ID 3
    3: {
        "nombre": "George Orwell",
        "nacionalidad": "Británica",
        "nacimiento": 1903
    }
}

# =========================================
# LIBROS
# =========================================

# Aquí se guardan los libros.
# La clave principal es el ISBN del libro.

biblioteca["libros"] = {

    # Libro 1
    "9780307474728": {
        "titulo": "Cien años de soledad",
        "anio": 1967,

        # Lista de autores del libro
        # El número 1 hace referencia al autor con ID 1
        "autores": [1],

        # Set de categorías
        "categorias": {"Novela", "Realismo mágico"},

        # Total de copias del libro
        "copias_totales": 5,

        # Copias disponibles actualmente
        "copias_disponibles": 3,

        # Cantidad de veces prestado
        "veces_prestado": 2
    },

    # Libro 2
    "9788478884452": {
        "titulo": "Harry Potter y la piedra filosofal",
        "anio": 1997,
        "autores": [2],
        "categorias": {"Fantasía", "Aventura"},
        "copias_totales": 8,
        "copias_disponibles": 6,
        "veces_prestado": 2
    },

    # Libro 3
    "9780451524935": {
        "titulo": "1984",
        "anio": 1949,
        "autores": [3],
        "categorias": {"Distopía", "Política"},
        "copias_totales": 4,
        "copias_disponibles": 3,
        "veces_prestado": 1
    },

    # Libro 4
    "9780307389732": {
        "titulo": "Rebelión en la granja",
        "anio": 1945,
        "autores": [3],
        "categorias": {"Sátira", "Política"},
        "copias_totales": 3,
        "copias_disponibles": 3,
        "veces_prestado": 0
    },

    # Libro 5
    "9788498382662": {
        "titulo": "Harry Potter y la cámara secreta",
        "anio": 1998,
        "autores": [2],
        "categorias": {"Fantasía", "Aventura"},
        "copias_totales": 6,
        "copias_disponibles": 5,
        "veces_prestado": 1
    }
}

# =========================================
# USUARIOS
# =========================================

# Aquí se guardan los usuarios de la biblioteca.

biblioteca["usuarios"] = {

    # Usuario con ID 101
    101: {
        "nombre": "Carlos Fadul",
        "email": "carlos@example.com",
        "telefono": "3001111111"
    },

    # Usuario con ID 102
    102: {
        "nombre": "Ana Gómez",
        "email": "ana@example.com",
        "telefono": "3002222222"
    },

    # Usuario con ID 103
    103: {
        "nombre": "Luis Pérez",
        "email": "luis@example.com",
        "telefono": "3003333333"
    },

    # Usuario con ID 104
    104: {
        "nombre": "María Torres",
        "email": "maria@example.com",
        "telefono": "3004444444"
    }
}

# =========================================
# PRÉSTAMOS
# =========================================

# Aquí se guardan los préstamos de libros.

biblioteca["prestamos"] = {

    # Préstamo 1
    1: {

        # ID del usuario que pidió el libro
        "usuario_id": 101,

        # ISBN del libro prestado
        "isbn": "9780307474728",

        # Fecha del préstamo
        "fecha_prestamo": (2026, 4, 1),

        # Fecha de devolución
        "fecha_devolucion": (2026, 4, 15),

        # Estado del préstamo
        "estado": "devuelto"
    },

    # Préstamo 2
    2: {
        "usuario_id": 102,
        "isbn": "9788478884452",
        "fecha_prestamo": (2026, 5, 1),
        "fecha_devolucion": (2026, 5, 15),
        "estado": "activo"
    },

    # Préstamo 3
    3: {
        "usuario_id": 103,
        "isbn": "9780451524935",
        "fecha_prestamo": (2026, 4, 20),
        "fecha_devolucion": (2026, 5, 5),
        "estado": "atrasado"
    }
}

# =========================================
# MOSTRAR LIBROS DISPONIBLES
# =========================================

print("=" * 60)
print("LIBROS DISPONIBLES")
print("=" * 60)

# Recorremos todos los libros
for isbn, libro in biblioteca["libros"].items():

    # Verificamos si tiene copias disponibles
    if libro["copias_disponibles"] > 0:

        # Mostramos título y cantidad disponible
        print(f"{libro['titulo']} - Disponibles: {libro['copias_disponibles']}")

# =========================================
# MOSTRAR LIBROS DE GEORGE ORWELL
# =========================================

print("\n" + "=" * 60)
print("LIBROS DE GEORGE ORWELL")
print("=" * 60)

# ID del autor George Orwell
autor_id = 3

# Recorremos todos los libros
for isbn, libro in biblioteca["libros"].items():

    # Verificamos si el autor está en la lista de autores
    if autor_id in libro["autores"]:

        # Mostramos el título
        print(libro["titulo"])

# =========================================
# MOSTRAR PRÉSTAMOS ACTIVOS
# =========================================

print("\n" + "=" * 60)
print("PRÉSTAMOS ACTIVOS")
print("=" * 60)

# Recorremos los préstamos
for prestamo_id, prestamo in biblioteca["prestamos"].items():

    # Verificamos si está activo
    if prestamo["estado"] == "activo":

        # Buscamos el nombre del usuario
        usuario = biblioteca["usuarios"][prestamo["usuario_id"]]["nombre"]

        # Buscamos el título del libro
        libro = biblioteca["libros"][prestamo["isbn"]]["titulo"]

        # Mostramos la información
        print(f"Préstamo {prestamo_id}: {usuario} -> {libro}")

# =========================================
# USUARIOS CON PRÉSTAMOS ATRASADOS
# =========================================

print("\n" + "=" * 60)
print("USUARIOS CON PRÉSTAMOS ATRASADOS")
print("=" * 60)

# Recorremos los préstamos
for prestamo in biblioteca["prestamos"].values():

    # Verificamos si está atrasado
    if prestamo["estado"] == "atrasado":

        # Obtenemos el nombre del usuario
        usuario = biblioteca["usuarios"][prestamo["usuario_id"]]["nombre"]

        print(usuario)

# =========================================
# MOSTRAR CATEGORÍAS EXISTENTES
# =========================================

print("\n" + "=" * 60)
print("CATEGORÍAS EXISTENTES")
print("=" * 60)

# Creamos un set vacío para evitar categorías repetidas
categorias = set()

# Recorremos todos los libros
for libro in biblioteca["libros"].values():

    # Agregamos las categorías al set
    categorias.update(libro["categorias"])

# sorted() ordena alfabéticamente
for categoria in sorted(categorias):
    print(categoria)

# =========================================
# LIBRO MÁS PRESTADO
# =========================================

print("\n" + "=" * 60)
print("LIBRO MÁS PRESTADO")
print("=" * 60)

# max() busca el libro con mayor número de préstamos
isbn_mas_prestado = max(

    # Lista de libros
    biblioteca["libros"],

    # Se compara usando veces_prestado
    key=lambda isbn: biblioteca["libros"][isbn]["veces_prestado"]
)

# Mostramos el título del libro más prestado
print(biblioteca["libros"][isbn_mas_prestado]["titulo"])

# =========================================
# TOTAL DE COPIAS EN LA BIBLIOTECA
# =========================================

print("\n" + "=" * 60)
print("TOTAL DE COPIAS EN LA BIBLIOTECA")
print("=" * 60)

# Variable acumuladora
total_copias = 0

# Recorremos los libros
for libro in biblioteca["libros"].values():

    # Sumamos las copias totales
    total_copias += libro["copias_totales"]

# Mostramos el total
print(total_copias)

# =========================================
# TOTAL DE PRÉSTAMOS ACTIVOS
# =========================================

print("\n" + "=" * 60)
print("TOTAL DE PRÉSTAMOS ACTIVOS")
print("=" * 60)

# Contador
activos = 0

# Recorremos los préstamos
for prestamo in biblioteca["prestamos"].values():

    # Verificamos si está activo
    if prestamo["estado"] == "activo":

        # Sumamos 1
        activos += 1

# Mostramos el total
print(activos)

# =========================================
# HISTORIAL DE PRÉSTAMOS POR USUARIO
# =========================================

print("\n" + "=" * 60)
print("HISTORIAL DE PRÉSTAMOS POR USUARIO")
print("=" * 60)

# Recorremos todos los usuarios
for usuario_id, usuario in biblioteca["usuarios"].items():

    # Mostramos el nombre del usuario
    print(f"\n{usuario['nombre']}:")

    # Variable para saber si tiene préstamos
    tiene_prestamos = False

    # Recorremos los préstamos
    for prestamo in biblioteca["prestamos"].values():

        # Verificamos si el préstamo pertenece al usuario
        if prestamo["usuario_id"] == usuario_id:

            # Buscamos el título del libro
            titulo = biblioteca["libros"][prestamo["isbn"]]["titulo"]

            # Mostramos título y estado
            print(f" - {titulo} ({prestamo['estado']})")

            # Indicamos que sí tiene préstamos
            tiene_prestamos = True

    # Si no tiene préstamos
    if not tiene_prestamos:
        print(" - Sin préstamos")
        