"""
Crear una aplicación que permita:

Registrar usuarios.
Validar información.
Guardar en archivo.
Capturar errores.
Mostrar mensajes amigables.
"""

import csv

ARCHIVO = "usuarios.csv"


def registrar_usuario(usuarios):
    nombre = input("Ingrese el nombre: ").strip()

    if nombre == "":
        print("El nombre no puede estar vacío.")
        return

    correo = input("Ingrese el correo: ").strip()

    if correo == "":
        print("El correo no puede estar vacío.")
        return

    try:
        edad = int(input("Ingrese la edad: "))

        usuario = {
            "nombre": nombre,
            "correo": correo,
            "edad": edad
        }

        usuarios.append(usuario)

        print("Usuario registrado correctamente.")

    except ValueError:
        print("Error: la edad debe ser un número entero.")


def mostrar_usuarios(usuarios):
    if len(usuarios) == 0:
        print("No hay usuarios registrados.")
        return

    print("\n--- LISTA DE USUARIOS ---")

    for i, usuario in enumerate(usuarios, start=1):
        print(f"{i}. Nombre: {usuario['nombre']}")
        print(f"   Correo: {usuario['correo']}")
        print(f"   Edad: {usuario['edad']}")


def validar_usuarios(usuarios):
    if len(usuarios) == 0:
        print("No hay usuarios para validar.")
        return False

    errores = 0
    correos = []

    for usuario in usuarios:
        nombre = usuario["nombre"].strip()
        correo = usuario["correo"].strip()
        edad = usuario["edad"]

        if nombre == "":
            print("Error: existe un usuario sin nombre.")
            errores += 1

        if "@" not in correo:
            print(f"Error: correo inválido -> {correo}")
            errores += 1

        if edad <= 0:
            print(f"Error: edad inválida para {nombre}")
            errores += 1

        if correo.lower() in correos:
            print(f"Error: correo duplicado -> {correo}")
            errores += 1
        else:
            correos.append(correo.lower())

    if errores == 0:
        print("Todos los usuarios son válidos.")
        return True
    else:
        print(f"Se encontraron {errores} errores.")
        return False


def guardar_csv(usuarios):
    if len(usuarios) == 0:
        print("No hay usuarios para guardar.")
        return

    if validar_usuarios(usuarios) == False:
        print("No se pueden guardar los datos.")
        return

    try:
        with open(ARCHIVO, "w", newline="", encoding="utf-8") as archivo:
            campos = ["nombre", "correo", "edad"]

            escritor = csv.DictWriter(
                archivo,
                fieldnames=campos
            )

            escritor.writeheader()
            escritor.writerows(usuarios)

        print("Usuarios guardados correctamente en usuarios.csv.")

    except Exception as error:
        print("Ocurrió un error al guardar el archivo.")
        print(error)


def buscar_usuario(usuarios):
    nombre = input("Ingrese el nombre a buscar: ").strip().lower()

    encontrados = []

    for usuario in usuarios:
        if nombre in usuario["nombre"].lower():
            encontrados.append(usuario)

    if len(encontrados) == 0:
        print("No se encontraron usuarios.")
    else:
        print("\n--- USUARIOS ENCONTRADOS ---")

        for usuario in encontrados:
            print(f"Nombre: {usuario['nombre']}")
            print(f"Correo: {usuario['correo']}")
            print(f"Edad: {usuario['edad']}")


def mostrar_menu():
    print("\n===== SISTEMA DE USUARIOS =====")
    print("1. Registrar usuario")
    print("2. Mostrar usuarios")
    print("3. Buscar usuario")
    print("4. Validar información")
    print("5. Guardar en CSV")
    print("6. Salir")


def ejecutar_programa():
    usuarios = []

    opcion = ""

    while opcion != "6":

        mostrar_menu()

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_usuario(usuarios)

        elif opcion == "2":
            mostrar_usuarios(usuarios)

        elif opcion == "3":
            buscar_usuario(usuarios)

        elif opcion == "4":
            validar_usuarios(usuarios)

        elif opcion == "5":
            guardar_csv(usuarios)

        elif opcion == "6":
            print("Gracias por utilizar el sistema.")

        else:
            print("Opción inválida. Intente nuevamente.")


ejecutar_programa()