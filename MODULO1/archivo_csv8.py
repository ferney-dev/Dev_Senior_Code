#           """
# Crear un sistema que permita:

# 1. Registrar productos con su nombre, precio y cantidad.
# 2. Mostrar inventario
# 3. Buscar productos
# 4. Validar datos
# 5. Guardar información en csv
# 6. Terminar

# La estructura sería:

# nombre, precio, cantidad
# """ 

import csv

# Lista donde se almacenan los productos
inventario = []


# ==========================
# REGISTRAR PRODUCTO
# ==========================
def registrar_producto():
    try:
        nombre = input("Ingrese el nombre del producto: ").strip()

        if not nombre:
            print("El nombre no puede estar vacío.")
            return

        precio = float(input("Ingrese el precio: "))
        cantidad = int(input("Ingrese la cantidad: "))

        if precio < 0 or cantidad < 0:
            print("El precio y la cantidad no pueden ser negativos.")
            return

        producto = {
            "nombre": nombre,
            "precio": precio,
            "cantidad": cantidad
        }

        inventario.append(producto)
        print("Producto registrado correctamente.")

    except ValueError:
        print("Error: Debe ingresar valores numéricos válidos.")


# ==========================
# MOSTRAR INVENTARIO
# ==========================
def mostrar_inventario():
    if len(inventario) == 0:
        print("No hay productos registrados.")
        return

    print("\n===== INVENTARIO =====")

    for producto in inventario:
        print(
            f"Nombre: {producto['nombre']} | "
            f"Precio: ${producto['precio']} | "
            f"Cantidad: {producto['cantidad']}"
        )


# ==========================
# BUSCAR PRODUCTO
# ==========================
def buscar_producto():
    nombre_buscar = input(
        "Ingrese el nombre del producto a buscar: "
    ).strip().lower()

    encontrado = False

    for producto in inventario:
        if producto["nombre"].lower() == nombre_buscar:
            print("\nProducto encontrado:")
            print(
                f"Nombre: {producto['nombre']} | "
                f"Precio: ${producto['precio']} | "
                f"Cantidad: {producto['cantidad']}"
            )
            encontrado = True

    if not encontrado:
        print("Producto no encontrado.")


# ==========================
# GUARDAR EN CSV
# ==========================
def guardar_csv():
    try:
        with open(
            "inventario.csv",
            "w",
            newline="",
            encoding="utf-8"
        ) as archivo:

            campos = ["nombre", "precio", "cantidad"]

            escritor = csv.DictWriter(
                archivo,
                fieldnames=campos
            )

            escritor.writeheader()

            for producto in inventario:
                escritor.writerow(producto)

        print("Inventario guardado correctamente.")

    except Exception as error:
        print("Error al guardar:", error)


# ==========================
# CARGAR CSV
# ==========================
def cargar_csv():
    try:
        with open(
            "inventario.csv",
            "r",
            encoding="utf-8"
        ) as archivo:

            lector = csv.DictReader(archivo)

            for fila in lector:
                try:
                    nombre = fila["nombre"]
                    precio = float(fila["precio"])
                    cantidad = int(fila["cantidad"])

                    if precio < 0 or cantidad < 0:
                        print("Fila inválida:", fila)
                        continue

                    inventario.append({
                        "nombre": nombre,
                        "precio": precio,
                        "cantidad": cantidad
                    })

                except (ValueError, TypeError):
                    print(
                        "Error de formato en la fila:",
                        fila
                    )

                except KeyError:
                    print(
                        "Falta una columna en la fila:",
                        fila
                    )

    except FileNotFoundError:
        pass


# ==========================
# MENÚ PRINCIPAL
# ==========================
def menu():
    cargar_csv()

    while True:
        print("\n===== SISTEMA DE INVENTARIO =====")
        print("1. Registrar producto")
        print("2. Mostrar inventario")
        print("3. Buscar producto")
        print("4. Guardar información en CSV")
        print("5. Terminar")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_producto()

        elif opcion == "2":
            mostrar_inventario()

        elif opcion == "3":
            buscar_producto()

        elif opcion == "4":
            guardar_csv()

        elif opcion == "5":
            guardar_csv()
            print("Programa finalizado.")
            break

        else:
            print("Opción inválida.")


# ==========================
# INICIO DEL PROGRAMA
# ==========================
menu()