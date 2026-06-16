# ============================================
# SISTEMA DE REGISTRO DE TAREAS
# Manejo de archivos, ciclos, condicionales,
# listas y funciones
# ============================================

NOMBRE_ARCHIVO = "tareas.txt"


def cargar_tareas():
    """
    Lee las tareas guardadas en el archivo tareas.txt.
    Si el archivo no existe, retorna una lista vacía.
    """
    try:
        with open(NOMBRE_ARCHIVO, "r", encoding="utf-8") as archivo:
            tareas = archivo.readlines()

        # Eliminamos saltos de línea con strip()
        tareas_limpias = []

        for tarea in tareas:
            tareas_limpias.append(tarea.strip())

        return tareas_limpias

    except FileNotFoundError:
        return []


def guardar_tarea(tarea):
    """
    Guarda una nueva tarea al final del archivo.
    """
    with open(NOMBRE_ARCHIVO, "a", encoding="utf-8") as archivo:
        archivo.write(tarea + "\n")


def agregar_tarea():
    """
    Solicita una tarea al usuario y la guarda en el archivo.
    """
    tarea = input("Ingrese la nueva tarea: ")

    if tarea.strip() == "":
        print("No se puede guardar una tarea vacía.")
    else:
        guardar_tarea(tarea)
        print("Tarea guardada correctamente.")


def mostrar_tareas():
    """
    Muestra todas las tareas guardadas.
    """
    tareas = cargar_tareas()

    if len(tareas) == 0:
        print("No hay tareas registradas.")
    else:
        print("\n--- LISTADO DE TAREAS ---")

        for indice, tarea in enumerate(tareas, start=1):
            print(f"{indice}. {tarea}")


def buscar_tarea():
    """
    Busca tareas que contengan una palabra clave.
    """
    tareas = cargar_tareas()

    if len(tareas) == 0:
        print("No hay tareas para buscar.")
    else:
        palabra = input("Ingrese palabra clave para buscar: ").lower()

        encontradas = []

        for tarea in tareas:
            if palabra in tarea.lower():
                encontradas.append(tarea)

        if len(encontradas) == 0:
            print("No se encontraron tareas con esa palabra.")
        else:
            print("\n--- TAREAS ENCONTRADAS ---")
            for indice, tarea in enumerate(encontradas, start=1):
                print(f"{indice}. {tarea}")


def contar_tareas():
    """
    Cuenta cuántas tareas hay registradas.
    """
    tareas = cargar_tareas()
    print(f"Total de tareas registradas: {len(tareas)}")


def mostrar_menu():
    """
    Muestra el menú principal del sistema.
    """
    print("\n===== SISTEMA DE REGISTRO DE TAREAS =====")
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Buscar tarea")
    print("4. Contar tareas")
    print("5. Salir")


def ejecutar_programa():
    """
    Ejecuta el sistema usando un ciclo while.
    """
    opcion = ""

    while opcion != "5":
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_tarea()

        elif opcion == "2":
            mostrar_tareas()

        elif opcion == "3":
            buscar_tarea()

        elif opcion == "4":
            contar_tareas()

        elif opcion == "5":
            print("Programa finalizado. Hasta pronto.")

        else:
            print("Opción inválida. Intente nuevamente.")


# Punto de inicio del programa
ejecutar_programa()