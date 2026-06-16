"""
Crear una aplicación que permita:

Registrar usuarios.
Validar información.
Guardar en archivo.
Capturar errores.
Mostrar mensajes amigables.

carlos,25
ana,301

pedro,22

Modificar el programa para:

Buscar usuarios.
Evitar usuarios duplicados.
Validar un archivo al momento de leerlo y en caso de errores mortralos
Crear archivo de errores. Meter los datos buenos en un archivo y los malos en otro
Registrar fecha y hora de creación.

 Pilas!!! en la opción de validar un archivo, yo les voy a pasar un archivo con errores y esa opción me va a mostrar los errores.
 En la opción de crear un archivo de errores, yo les voy a pasar un archivo con errores y esa opción me va a crear un archivo con los registros malos y un archivo con los registros buenos
 Registrar fecha lo que implica es modificar la función que ya tenemos de registrar usuario para que cada que se registre un usuario se agregue la fecha y hora del momento

Carlos,25,2026-06-12 16:31:07
Maria,-52,2026-06-12 16:31:21
Miguel,24,2026-06-12 16:31:31
,23,2026-06-12 16:31:38
Manuela,19,2026-06-12 16:32:05
Felipe,148,2026-06-12 16:32:22
Valentina,30,2026-06-12 16:32:31
Modificar el programa para:

Buscar usuarios.
Evitar usuarios duplicados.
Validar un archivo al momento de leerlo y en caso de errores mortralos
Crear archivo de errores. Meter los datos buenos en un archivo y los malos en otro
Registrar fecha y hora de creación.

"""
import datetime

ARCHIVO = "usuarios.txt"
ARCHIVO_BUENOS = "usuarios_buenos.txt"
ARCHIVO_MALOS = "usuarios_malos.txt"


# ==========================
# REGISTRAR USUARIO
# ==========================
def registrar_usuario():

    try:

        nombre = input("Ingrese el nombre: ").strip()

        if nombre == "":
            print("El nombre no puede estar vacío.")
            return

        edad = int(input("Ingrese la edad: "))

        if edad < 0:
            print("La edad no puede ser negativa.")
            return

        if edad > 120:
            print("La edad es inválida.")
            return

        # Verificar duplicados
        try:

            with open(ARCHIVO, "r", encoding="utf-8") as archivo:

                for linea in archivo:

                    datos = linea.strip().split(",")

                    if datos[0].lower() == nombre.lower():

                        print("Ese usuario ya existe.")
                        return

        except FileNotFoundError:
            pass

        fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open(ARCHIVO, "a", encoding="utf-8") as archivo:
            archivo.write(f"{nombre},{edad},{fecha}\n")

        print("Usuario registrado correctamente.")

    except ValueError:
        print("La edad debe ser numérica.")

    except PermissionError:
        print("No tiene permisos para escribir el archivo.")

    except Exception as error:
        print("Error:", error)


# ==========================
# BUSCAR USUARIO
# ==========================
def buscar_usuario():

    nombre_buscar = input("Ingrese el nombre a buscar: ")

    encontrado = False

    try:

        with open(ARCHIVO, "r", encoding="utf-8") as archivo:

            for linea in archivo:

                datos = linea.strip().split(",")

                if datos[0].lower() == nombre_buscar.lower():

                    print("\nUsuario encontrado:")
                    print("Nombre:", datos[0])
                    print("Edad:", datos[1])
                    print("Fecha:", datos[2])

                    encontrado = True

        if not encontrado:
            print("Usuario no encontrado.")

    except FileNotFoundError:
        print("El archivo no existe.")

    except PermissionError:
        print("No tiene permisos para leer el archivo.")

    except Exception as error:
        print("Error:", error)


# ==========================
# MOSTRAR USUARIOS
# ==========================
def mostrar_usuarios():

    try:

        with open(ARCHIVO, "r", encoding="utf-8") as archivo:

            lineas = archivo.readlines()

            if len(lineas) == 0:

                print("No hay usuarios registrados.")
                return

            print("\n===== USUARIOS =====")

            for linea in lineas:

                datos = linea.strip().split(",")

                if len(datos) >= 3:

                    print(
                        "Nombre:", datos[0],
                        "| Edad:", datos[1],
                        "| Fecha:", datos[2]
                    )

    except FileNotFoundError:
        print("El archivo no existe.")

    except PermissionError:
        print("No tiene permisos para leer.")

    except Exception as error:
        print("Error:", error)


# ==========================
# VALIDAR ARCHIVO
# ==========================
def validar_archivo():

    nombre_archivo = input("Ingrese el archivo: ")

    try:

        with open(nombre_archivo, "r", encoding="utf-8") as archivo:

            errores = []

            for numero, linea in enumerate(archivo, start=1):

                if linea.strip() == "":
                    continue

                datos = linea.strip().split(",")

                if len(datos) < 3:

                    errores.append(
                        f"Línea {numero}: Formato incorrecto"
                    )

                    continue

                nombre = datos[0]

                try:

                    edad = int(datos[1])

                    if nombre == "":
                        errores.append(
                            f"Línea {numero}: Nombre vacío"
                        )

                    if edad < 0:
                        errores.append(
                            f"Línea {numero}: Edad negativa"
                        )

                    if edad > 120:
                        errores.append(
                            f"Línea {numero}: Edad mayor a 120"
                        )

                except ValueError:

                    errores.append(
                        f"Línea {numero}: Edad no numérica"
                    )

            if len(errores) == 0:

                print("No se encontraron errores.")

            else:

                print("\n===== ERRORES =====")

                for error in errores:
                    print(error)

    except FileNotFoundError:
        print("El archivo no existe.")

    except PermissionError:
        print("No tiene permisos.")

    except Exception as error:
        print("Error:", error)


# ==========================
# CREAR ARCHIVO DE ERRORES
# ==========================
def separar_archivo():

    nombre_archivo = input("Ingrese el archivo: ")

    buenos = []
    malos = []

    try:

        with open(nombre_archivo, "r", encoding="utf-8") as archivo:

            for linea in archivo:

                if linea.strip() == "":
                    continue

                datos = linea.strip().split(",")

                if len(datos) < 3:

                    malos.append(
                        linea.strip() + " --> Formato incorrecto\n"
                    )

                    continue

                nombre = datos[0]

                try:

                    edad = int(datos[1])

                    if nombre == "":

                        malos.append(
                            linea.strip() + " --> Nombre vacío\n"
                        )

                    elif edad < 0:

                        malos.append(
                            linea.strip() + " --> Edad negativa\n"
                        )

                    elif edad > 120:

                        malos.append(
                            linea.strip() + " --> Edad mayor a 120\n"
                        )

                    else:

                        buenos.append(linea)

                except ValueError:

                    malos.append(
                        linea.strip() + " --> Edad no numérica\n"
                    )

        with open(ARCHIVO_BUENOS, "w", encoding="utf-8") as archivo:

            for linea in buenos:
                archivo.write(linea)

        with open(ARCHIVO_MALOS, "w", encoding="utf-8") as archivo:

            for linea in malos:
                archivo.write(linea)

        print("\nProceso completado.")
        print("usuarios_buenos.txt creado.")
        print("usuarios_malos.txt creado.")
        print("Buenos:", len(buenos))
        print("Malos:", len(malos))

    except FileNotFoundError:
        print("El archivo no existe.")

    except PermissionError:
        print("No tiene permisos.")

    except Exception as error:
        print("Error:", error)


# ==========================
# CONTAR USUARIOS
# ==========================
def cantidad_usuarios():

    try:

        with open(ARCHIVO, "r", encoding="utf-8") as archivo:

            print("Cantidad de usuarios:",
                  len(archivo.readlines()))

    except:
        print("No se pudo leer el archivo.")


# ==========================
# ELIMINAR USUARIO
# ==========================
def eliminar_usuario():

    nombre = input("Nombre a eliminar: ")

    try:

        with open(ARCHIVO, "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()

        encontrado = False

        with open(ARCHIVO, "w", encoding="utf-8") as archivo:

            for linea in lineas:

                datos = linea.strip().split(",")

                if datos[0].lower() != nombre.lower():
                    archivo.write(linea)

                else:
                    encontrado = True

        if encontrado:
            print("Usuario eliminado.")
        else:
            print("Usuario no encontrado.")

    except:
        print("Error al eliminar.")


# ==========================
# MENU
# ==========================
def menu():

    while True:

        print("\n======================")
        print(" SISTEMA DE USUARIOS ")
        print("======================")
        print("1. Registrar usuario")
        print("2. Buscar usuario")
        print("3. Mostrar usuarios")
        print("4. Validar archivo")
        print("5. Crear archivo de errores")
        print("6. Cantidad de usuarios")
        print("7. Eliminar usuario")
        print("8. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_usuario()

        elif opcion == "2":
            buscar_usuario()

        elif opcion == "3":
            mostrar_usuarios()

        elif opcion == "4":
            validar_archivo()

        elif opcion == "5":
            separar_archivo()

        elif opcion == "6":
            cantidad_usuarios()

        elif opcion == "7":
            eliminar_usuario()

        elif opcion == "8":
            print("Programa finalizado.")
            break

        else:
            print("Opción inválida.")


menu()