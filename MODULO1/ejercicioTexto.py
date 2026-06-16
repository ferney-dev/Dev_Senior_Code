"""
Enunciado del ejercicio

Desarrolla un programa llamado Sistema de Registro de Tareas.

El programa debe permitir al usuario:

Agregar una nueva tarea.
Ver todas las tareas guardadas.
Buscar una tarea por palabra clave.
Contar cuántas tareas hay registradas.
Salir del programa.

Las tareas deben guardarse en un archivo llamado:

tareas.txt

Cada tarea debe almacenarse en una línea diferente.

Requisitos técnicos

El programa debe usar:

open()

Bloque seguro:

with open(...)

Funciones:

agregar_tarea()
mostrar_tareas()
buscar_tarea()
contar_tareas()

Un ciclo while para mantener activo el menú.

Condicionales if, elif, else para controlar las opciones.

Una lista para almacenar temporalmente las tareas leídas desde el archivo.

Ejemplo de ejecución esperada
===== SISTEMA DE REGISTRO DE TAREAS =====
1. Agregar tarea
2. Ver tareas
3. Buscar tarea
4. Contar tareas
5. Salir

Seleccione una opción: 1
Ingrese la nueva tarea: Estudiar manejo de archivos en Python
Tarea guardada correctamente.

Seleccione una opción: 2

--- LISTADO DE TAREAS ---
1. Estudiar manejo de archivos en Python
2. Comprar materiales para clase
3. Revisar ejercicios pendientes

Retos adicionales para estudiantes
Agregar una opción para eliminar tareas.
Agregar una opción para marcar tareas como completadas.
Guardar cada tarea con fecha.
Evitar tareas repetidas.
Mostrar solo tareas pendientes.
""""""
Sistema de Registro de Tareas
"""

# Función para agregar tareas
def agregar_tarea():
    tarea = input("Ingrese la nueva tarea: ")

    with open("tareas.txt", "a", encoding="utf-8") as archivo:
        archivo.write(tarea + "\n")

    print("Tarea guardada correctamente.")


# Función para mostrar tareas
def mostrar_tareas():

    try:
        with open("tareas.txt", "r", encoding="utf-8") as archivo:

            # Guardamos las tareas en una lista
            tareas = archivo.readlines()

            if len(tareas) > 0:

                print("\n--- LISTADO DE TAREAS ---")

                # enumerate sirve para numerar las tareas
                for indice, tarea in enumerate(tareas, start=1):
                    print(f"{indice}. {tarea.strip()}")

            else:
                print("No hay tareas registradas.")

    except FileNotFoundError:
        print("El archivo aún no existe.")


# Función para buscar tareas
def buscar_tarea():

    palabra = input("Ingrese una palabra clave: ")

    try:
        with open("tareas.txt", "r", encoding="utf-8") as archivo:

            tareas = archivo.readlines()

            encontradas = []

            # Recorremos las tareas
            for tarea in tareas:

                # lower() evita problemas con mayúsculas
                if palabra.lower() in tarea.lower():
                    encontradas.append(tarea.strip())

            # Mostramos resultados
            if len(encontradas) > 0:

                print("\n--- TAREAS ENCONTRADAS ---")

                for indice, tarea in enumerate(encontradas, start=1):
                    print(f"{indice}. {tarea}")

            else:
                print("No se encontraron tareas.")

    except FileNotFoundError:
        print("El archivo aún no existe.")


# Función para contar tareas
def contar_tareas():

    try:
        with open("tareas.txt", "r", encoding="utf-8") as archivo:

            tareas = archivo.readlines()

            print(f"Total de tareas registradas: {len(tareas)}")

    except FileNotFoundError:
        print("El archivo aún no existe.")


# Función principal
def main():

    while True:

        print("\n===== SISTEMA DE REGISTRO DE TAREAS =====")
        print("1. Agregar tarea")
        print("2. Ver tareas")
        print("3. Buscar tarea")
        print("4. Contar tareas")
        print("5. Salir")

        opcion = input("\nSeleccione una opción: ")

        # Condicionales del menú
        if opcion == "1":
            agregar_tarea()

        elif opcion == "2":
            mostrar_tareas()

        elif opcion == "3":
            buscar_tarea()

        elif opcion == "4":
            contar_tareas()

        elif opcion == "5":
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida. Intente nuevamente.")


# Ejecutar programa
if __name__ == "__main__":
    main()