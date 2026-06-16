# Importamos datetime para poder guardar la fecha y hora actual
from datetime import datetime

# Nombre del archivo donde se guardarán las tareas
NOMBRE_ARCHIVO = "tareas.txt"


# Función para cargar todas las tareas del archivo
def cargar_tareas():

    # Lista vacía donde se almacenarán las tareas
    tareas = []

    # Intentamos abrir el archivo
    try:

        # Abrimos el archivo en modo lectura
        with open(NOMBRE_ARCHIVO, "r", encoding="utf-8") as archivo:

            # Leemos todas las líneas del archivo
            lineas = archivo.readlines()

        # Recorremos cada línea del archivo
        for linea in lineas:

            # Eliminamos saltos de línea y dividimos usando |
            partes = linea.strip().split("|")

            # Verificamos que la línea tenga 3 datos
            if len(partes) == 3:

                # Creamos un diccionario con la información de la tarea
                tarea = {
                    "descripcion": partes[0],
                    "estado": partes[1],
                    "fecha": partes[2]
                }

                # Agregamos la tarea a la lista
                tareas.append(tarea)

    # Si el archivo no existe, evitamos que el programa falle
    except FileNotFoundError:
        pass

    # Retornamos la lista de tareas
    return tareas


# Función para guardar todas las tareas en el archivo
def guardar_todas_las_tareas(tareas):

    # Abrimos el archivo en modo escritura
    with open(NOMBRE_ARCHIVO, "w", encoding="utf-8") as archivo:

        # Recorremos cada tarea de la lista
        for tarea in tareas:

            # Convertimos la tarea en una línea de texto
            linea = f"{tarea['descripcion']}|{tarea['estado']}|{tarea['fecha']}\n"

            # Guardamos la línea en el archivo
            archivo.write(linea)


# Función para agregar una nueva tarea
def agregar_tarea():

    # Cargamos las tareas existentes
    tareas = cargar_tareas()

    # Pedimos la descripción de la nueva tarea
    descripcion = input("Ingrese la nueva tarea: ").strip()

    # Verificamos que no esté vacía
    if descripcion == "":
        print("No se puede guardar una tarea vacía.")
        return

    # Recorremos las tareas existentes
    for tarea in tareas:

        # Verificamos si la tarea ya existe
        if tarea["descripcion"].lower() == descripcion.lower():
            print("Esa tarea ya existe.")
            return

    # Creamos un diccionario para la nueva tarea
    nueva_tarea = {

        # Descripción escrita por el usuario
        "descripcion": descripcion,

        # Estado inicial de la tarea
        "estado": "pendiente",

        # Fecha y hora actual
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    # Agregamos la nueva tarea a la lista
    tareas.append(nueva_tarea)

    # Guardamos nuevamente todas las tareas
    guardar_todas_las_tareas(tareas)

    # Mensaje de confirmación
    print("Tarea guardada correctamente.")


# Función para mostrar todas las tareas
def mostrar_tareas():

    # Cargamos las tareas
    tareas = cargar_tareas()

    # Verificamos si no hay tareas
    if len(tareas) == 0:
        print("No hay tareas registradas.")
        return

    # Título de la sección
    print("\n--- LISTADO DE TAREAS ---")

    # Recorremos las tareas con numeración
    for i, tarea in enumerate(tareas, start=1):

        # Mostramos descripción
        print(f"{i}. {tarea['descripcion']}")

        # Mostramos estado
        print(f"   Estado: {tarea['estado']}")

        # Mostramos fecha
        print(f"   Fecha: {tarea['fecha']}")


# Función para mostrar tareas pendientes
def mostrar_pendientes():

    # Cargamos las tareas
    tareas = cargar_tareas()

    # Lista donde se guardarán las pendientes
    pendientes = []

    # Recorremos todas las tareas
    for tarea in tareas:

        # Verificamos si está pendiente
        if tarea["estado"] == "pendiente":

            # Agregamos la tarea a pendientes
            pendientes.append(tarea)

    # Verificamos si no hay pendientes
    if len(pendientes) == 0:
        print("No hay tareas pendientes.")
        return

    # Título de la sección
    print("\n--- TAREAS PENDIENTES ---")

    # Mostramos tareas pendientes
    for i, tarea in enumerate(pendientes, start=1):

        # Mostramos descripción
        print(f"{i}. {tarea['descripcion']}")

        # Mostramos fecha
        print(f"   Fecha: {tarea['fecha']}")


# Función para marcar tareas como completadas
def marcar_completada():

    # Cargamos las tareas
    tareas = cargar_tareas()

    # Verificamos si no existen tareas
    if len(tareas) == 0:
        print("No hay tareas registradas.")
        return

    # Mostramos las tareas
    mostrar_tareas()

    # Intentamos convertir el número ingresado
    try:

        # Pedimos el número de tarea
        numero = int(input("Ingrese el número de la tarea a completar: "))

        # Verificamos si el número es inválido
        if numero < 1 or numero > len(tareas):
            print("Número de tarea inválido.")
            return

        # Cambiamos el estado a completada
        tareas[numero - 1]["estado"] = "completada"

        # Guardamos las tareas actualizadas
        guardar_todas_las_tareas(tareas)

        # Mensaje de confirmación
        print("Tarea marcada como completada.")

    # Si el usuario escribe algo diferente a un número
    except ValueError:
        print("Debe ingresar un número válido.")


# Función para eliminar tareas
def eliminar_tarea():

    # Cargamos las tareas
    tareas = cargar_tareas()

    # Verificamos si no hay tareas
    if len(tareas) == 0:
        print("No hay tareas para eliminar.")
        return

    # Mostramos las tareas
    mostrar_tareas()

    # Intentamos convertir el valor ingresado a entero
    try:

        # Pedimos el número de tarea
        numero = int(input("Ingrese el número de la tarea a eliminar: "))

        # Verificamos si el número es inválido
        if numero < 1 or numero > len(tareas):
            print("Número de tarea inválido.")
            return

        # Eliminamos la tarea seleccionada
        tarea_eliminada = tareas.pop(numero - 1)

        # Guardamos nuevamente las tareas
        guardar_todas_las_tareas(tareas)

        # Mostramos mensaje de confirmación
        print(f"Tarea eliminada: {tarea_eliminada['descripcion']}")

    # Si el usuario escribe algo inválido
    except ValueError:
        print("Debe ingresar un número válido.")


# Función para buscar tareas
def buscar_tarea():

    # Cargamos las tareas
    tareas = cargar_tareas()

    # Verificamos si no hay tareas
    if len(tareas) == 0:
        print("No hay tareas para buscar.")
        return

    # Pedimos palabra clave y la convertimos a minúscula
    palabra = input("Ingrese palabra clave: ").lower()

    # Lista para guardar coincidencias
    encontradas = []

    # Recorremos las tareas
    for tarea in tareas:

        # Verificamos si la palabra existe en la descripción
        if palabra in tarea["descripcion"].lower():

            # Agregamos la tarea encontrada
            encontradas.append(tarea)

    # Verificamos si no hubo resultados
    if len(encontradas) == 0:
        print("No se encontraron tareas.")
        return

    # Título de resultados
    print("\n--- TAREAS ENCONTRADAS ---")

    # Mostramos las tareas encontradas
    for i, tarea in enumerate(encontradas, start=1):

        # Mostramos descripción
        print(f"{i}. {tarea['descripcion']}")

        # Mostramos estado
        print(f"   Estado: {tarea['estado']}")

        # Mostramos fecha
        print(f"   Fecha: {tarea['fecha']}")


# Función para contar tareas
def contar_tareas():

    # Cargamos las tareas
    tareas = cargar_tareas()

    # Total de tareas
    total = len(tareas)

    # Contador de pendientes
    pendientes = 0

    # Contador de completadas
    completadas = 0

    # Recorremos las tareas
    for tarea in tareas:

        # Verificamos si está pendiente
        if tarea["estado"] == "pendiente":

            # Sumamos 1
            pendientes += 1

        # Verificamos si está completada
        elif tarea["estado"] == "completada":

            # Sumamos 1
            completadas += 1

    # Mostramos el total
    print(f"Total de tareas: {total}")

    # Mostramos pendientes
    print(f"Pendientes: {pendientes}")

    # Mostramos completadas
    print(f"Completadas: {completadas}")


# Función para mostrar el menú principal
def mostrar_menu():

    # Mostramos opciones del sistema
    print("\n===== SISTEMA DE REGISTRO DE TAREAS =====")
    print("1. Agregar tarea")
    print("2. Ver todas las tareas")
    print("3. Buscar tarea")
    print("4. Contar tareas")
    print("5. Eliminar tarea")
    print("6. Marcar tarea como completada")
    print("7. Mostrar tareas pendientes")
    print("8. Salir")


# Función principal del programa
def ejecutar_programa():

    # Variable para guardar la opción
    opcion = ""

    # Ciclo que se ejecuta hasta elegir salir
    while opcion != "8":

        # Mostramos el menú
        mostrar_menu()

        # Pedimos una opción
        opcion = input("Seleccione una opción: ")

        # Verificamos cada opción
        if opcion == "1":
            agregar_tarea()

        elif opcion == "2":
            mostrar_tareas()

        elif opcion == "3":
            buscar_tarea()

        elif opcion == "4":
            contar_tareas()

        elif opcion == "5":
            eliminar_tarea()

        elif opcion == "6":
            marcar_completada()

        elif opcion == "7":
            mostrar_pendientes()

        elif opcion == "8":
            print("Programa finalizado.")

        # Si la opción no existe
        else:
            print("Opción inválida.")


# Ejecutamos el programa
ejecutar_programa()