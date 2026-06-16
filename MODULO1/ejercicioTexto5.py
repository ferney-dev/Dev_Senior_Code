import csv

ARCHIVO = "inventario.csv"


def registrar_producto(productos):
    nombre = input("Ingrese el nombre del producto: ").strip()

    if nombre == "":
        print("El nombre no puede estar vacío.")
        return

    try:
        precio = float(input("Ingrese el precio: "))
        cantidad = int(input("Ingrese la cantidad: "))

        producto = {
            "nombre": nombre,
            "precio": precio,
            "cantidad": cantidad
        }

        productos.append(producto)

        print("Producto registrado en memoria.")

    except ValueError:
        print("Error: el precio y la cantidad deben ser números.")


def mostrar_inventario(productos):
    if len(productos) == 0:
        print("No hay productos registrados.")
        return

    print("\n--- INVENTARIO ---")

    for i, producto in enumerate(productos, start=1):
        print(f"{i}. {producto['nombre']}")
        print(f"   Precio: ${producto['precio']:.2f}")
        print(f"   Cantidad: {producto['cantidad']}")


def buscar_producto(productos):
    if len(productos) == 0:
        print("No hay productos para buscar.")
        return

    palabra = input("Ingrese el nombre del producto a buscar: ").strip().lower()

    encontrados = []

    for producto in productos:
        if palabra in producto["nombre"].lower():
            encontrados.append(producto)

    if len(encontrados) == 0:
        print("No se encontraron productos.")
    else:
        print("\n--- PRODUCTOS ENCONTRADOS ---")

        for producto in encontrados:
            print(f"Producto: {producto['nombre']}")
            print(f"Precio: ${producto['precio']:.2f}")
            print(f"Cantidad: {producto['cantidad']}")


def validar_datos(productos):
    if len(productos) == 0:
        print("No hay productos para validar.")
        return False

    errores = 0
    nombres = []

    for producto in productos:
        nombre = producto["nombre"].strip()
        precio = producto["precio"]
        cantidad = producto["cantidad"]

        if nombre == "":
            print("Error: hay un producto con nombre vacío.")
            errores += 1

        if precio < 0:
            print(f"Error: el producto {nombre} tiene precio negativo.")
            errores += 1

        if cantidad < 0:
            print(f"Error: el producto {nombre} tiene cantidad negativa.")
            errores += 1

        if nombre.lower() in nombres:
            print(f"Error: producto duplicado: {nombre}")
            errores += 1
        else:
            nombres.append(nombre.lower())

    if errores == 0:
        print("Todos los datos son válidos.")
        return True
    else:
        print(f"Se encontraron {errores} error(es).")
        return False


def guardar_csv(productos):
    if len(productos) == 0:
        print("No hay productos para guardar.")
        return

    datos_validos = validar_datos(productos)

    if datos_validos == False:
        print("No se puede guardar porque hay datos inválidos.")
        return

    with open(ARCHIVO, "w", newline="", encoding="utf-8") as archivo:
        campos = ["nombre", "precio", "cantidad"]

        escritor = csv.DictWriter(archivo, fieldnames=campos)

        escritor.writeheader()

        escritor.writerows(productos)

    print("Inventario guardado correctamente en inventario.csv.")


def cargar_productos_iniciales():
    productos = [
        {
            "nombre": "Mouse",
            "precio": 120000,
            "cantidad": 10
        },
        {
            "nombre": "Teclado",
            "precio": -95000,
            "cantidad": -5
        },
        {
            "nombre": "Monitor",
            "precio": -250000,
            "cantidad": 3
        }
    ]

    return productos


def mostrar_menu():
    print("\n===== SISTEMA DE INVENTARIO CSV =====")
    print("1. Registrar productos")
    print("2. Mostrar inventario")
    print("3. Buscar productos")
    print("4. Validar datos")
    print("5. Guardar información en CSV")
    print("6. Terminar el programa")


def ejecutar_programa():
    productos = cargar_productos_iniciales()

    opcion = ""

    while opcion != "6":
        mostrar_menu()

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_producto(productos)

        elif opcion == "2":
            mostrar_inventario(productos)

        elif opcion == "3":
            buscar_producto(productos)

        elif opcion == "4":
            validar_datos(productos)

        elif opcion == "5":
            guardar_csv(productos)

        elif opcion == "6":
            print("Programa finalizado.")

        else:
            print("Opción inválida. Intente nuevamente.")


ejecutar_programa()