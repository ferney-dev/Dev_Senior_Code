"""Sistema de Gestión de Biblioteca
Enunciado completo

Desarrollar en Python un programa que permita gestionar una biblioteca usando estructuras compuestas de datos.

El programa debe utilizar:

Diccionarios
Listas
Diccionarios anidados
Listas de diccionarios
Restricciones

El programa debe cumplir estas condiciones:

No usar funciones.
No usar archivos.
No usar bases de datos.
Todo debe trabajarse en memoria.
El programa debe tener un menú interactivo.
El código debe estar documentado con comentarios.
Contexto

Una biblioteca necesita organizar la información de sus libros, usuarios y préstamos.

El sistema debe permitir registrar libros, registrar usuarios, prestar libros, devolver libros y 
consultar información general.

Estructura sugerida

El sistema debe manejar un diccionario principal llamado biblioteca con la siguiente estructura:

biblioteca = {
    "libros": {},
    "usuarios": {},
    "prestamos": []
}
Funcionalidades obligatorias
1. Agregar libro

El sistema debe solicitar:

Código del libro
Título
Autor
Año de publicación
Categoría

Cada libro debe guardarse con estado disponible.

2. Mostrar libros

Debe mostrar todos los libros registrados, indicando:

Código
Título
Autor
Año
Categoría
Disponibilidad
3. Eliminar libro

Debe permitir eliminar un libro por su código.

No se debe eliminar un libro si está prestado.

4. Registrar usuario

El sistema debe solicitar:

Código del usuario
Nombre
Teléfono
5. Mostrar usuarios

Debe mostrar todos los usuarios registrados.

6. Prestar libro

El sistema debe solicitar:

Código del usuario
Código del libro
Fecha de préstamo
Fecha estimada de entrega

Condiciones:

El usuario debe existir.
El libro debe existir.
El libro debe estar disponible.
Al prestarlo, el libro debe cambiar a no disponible.
El préstamo debe guardarse en una lista de préstamos.
7. Devolver libro

El sistema debe solicitar el código del libro.

Condiciones:

El libro debe existir.
El libro debe estar prestado.
Al devolverlo, debe cambiar nuevamente a disponible.
El préstamo activo debe marcarse como devuelto.
8. Mostrar préstamos activos

Debe mostrar solo los préstamos que aún no han sido devueltos.

9. Mostrar historial de préstamos

Debe mostrar todos los préstamos realizados, tanto activos como devueltos.

10. Salir

Finaliza el programa"""


# ==========================================================
# SISTEMA DE GESTIÓN DE BIBLIOTECA
# ==========================================================

# ----------------------------------------------------------
# DICCIONARIO PRINCIPAL
# ----------------------------------------------------------
# Aquí se guarda toda la información del sistema.
# "libros" guarda todos los libros.
# "usuarios" guarda todos los los usuarios.
# "prestamos" guarda todos los préstamos realizados.
# ----------------------------------------------------------

biblioteca = {
    "libros": {},      # Diccionario para guardar libros
    "usuarios": {},    # Diccionario para guardar usuarios
    "prestamos": []    # Lista para guardar préstamos
}
# ----------------------------------------------------------
# VARIABLE PARA CONTROLAR EL MENÚ
# ----------------------------------------------------------
# Esta variable almacenará la opción que el usuario elija.
# ----------------------------------------------------------
opcion = 0
# ----------------------------------------------------------
# CICLO PRINCIPAL DEL SISTEMA
# ----------------------------------------------------------
# El programa seguirá ejecutándose mientras la opción
# sea diferente de 10.
# ----------------------------------------------------------
while opcion != 10:
    # ======================================================
    # MENÚ PRINCIPAL
    # ======================================================
    print("\n========= BIBLIOTECA =========")
    print("1. Agregar libro")
    print("2. Mostrar libros")
    print("3. Eliminar libro")
    print("4. Registrar usuario")
    print("5. Mostrar usuarios")
    print("6. Prestar libro")
    print("7. Devolver libro")
    print("8. Mostrar préstamos activos")
    print("9. Mostrar historial")
    print("10. Salir")
    # Se pide al usuario seleccionar una opción.
    # int() convierte el dato ingresado en número entero.
    opcion = int(input("Seleccione una opción: "))
    
    # ======================================================
    # 1. AGREGAR LIBRO
    # ======================================================
    if opcion == 1:  
        # Solicitar información del libro
        codigo = input("Código del libro: ")
        titulo = input("Título: ")
        autor = input("Autor: ")
        anio = input("Año: ")
        categoria = input("Categoría: ")
        # Guardar libro dentro del diccionario "libros"
        # El código será la clave principal del libro.
        # Cada libro tendrá otro diccionario con sus datos.
        biblioteca["libros"][codigo] = {
            # Guardar título
            "titulo": titulo,
            # Guardar autor
            "autor": autor,
            # Guardar año
            "anio": anio,
            # Guardar categoría
            "categoria": categoria,
            # El libro inicia disponible
            "disponible": True
        }
        # Mensaje de confirmación
        print("✅ Libro agregado correctamente")

    # ======================================================
    # 2. MOSTRAR LIBROS
    # ======================================================
    elif opcion == 2:
        # Validar si no hay libros registrados
        if len(biblioteca["libros"]) == 0:
            print("No hay libros registrados")
        else:   
            # Recorrer todos los libros registrados
            # codigo = clave del libro
            # datos = información del libro
            for codigo, datos in biblioteca["libros"].items():# items devuelve clave y valor de un diccionario       
                # Estado inicial del libro
                estado = "Disponible"   
                # Si disponible es False, entonces está 
                # prestado
                if datos["disponible"] == False:
                    estado = "Prestado"
                # Mostrar información del libro
                print("\nCódigo:", codigo)
                print("Título:", datos["titulo"])
                print("Autor:", datos["autor"])
                print("Año:", datos["anio"])
                print("Categoría:", datos["categoria"])
                print("Estado:", estado)

    # ======================================================
    # 3. ELIMINAR LIBRO
    # ======================================================
    elif opcion == 3:
        # Solicitar código del libro
        codigo = input("Ingrese código del libro: ")
        # Validar si el libro existe
        if codigo in biblioteca["libros"]:  
            # Verificar si el libro está disponible
            if biblioteca["libros"][codigo]["disponible"] == True:    
                # Eliminar libro del diccionario
                # del elimina un elemento 
                del biblioteca["libros"][codigo]
                print("✅ Libro eliminado")
            else:
                # No se puede eliminar si está prestado
                print("❌ No se puede eliminar porque está prestado")
        else:  
            # Mensaje si el libro no existe
            print("❌ Libro no encontrado")

    # ======================================================
    # 4. REGISTRAR USUARIO
    # ======================================================
    elif opcion == 4:
        # Solicitar información del usuario
        codigo = input("Código usuario: ")
        nombre = input("Nombre: ")
        telefono = input("Teléfono: ")
        # Guardar usuario dentro del diccionario usuarios
        biblioteca["usuarios"][codigo] = {
            # Guardar nombre
            "nombre": nombre,
            # Guardar teléfono
            "telefono": telefono
        }
        print("✅ Usuario registrado")
        
    # ======================================================
    # 5. MOSTRAR USUARIOS
    # ======================================================

    elif opcion == 5:    
        # Verificar si no existen usuarios
        if len(biblioteca["usuarios"]) == 0:
            print("No hay usuarios")
        else:      
            # Recorrer todos los usuarios
            for codigo, datos in biblioteca["usuarios"].items():  
                # Mostrar información del usuario
                print("\nCódigo:", codigo)
                print("Nombre:", datos["nombre"])
                print("Teléfono:", datos["telefono"])

    # ======================================================
    # 6. PRESTAR LIBRO
    # ======================================================

    elif opcion == 6:
        # Solicitar información del préstamo
        codigo_usuario = input("Código usuario: ")
        codigo_libro = input("Código libro: ")
        fecha_prestamo = input("Fecha préstamo: ")
        fecha_entrega = input("Fecha entrega: ")

        # Validar si el usuario existe
        if codigo_usuario not in biblioteca["usuarios"]:
            print("❌ Usuario no existe")
        # Validar si el libro existe
        elif codigo_libro not in biblioteca["libros"]:
            print("❌ Libro no existe")

        # Verificar disponibilidad del libro
        elif biblioteca["libros"][codigo_libro]["disponible"] == False:
            print("❌ Libro no disponible")
        else:
 
        # Cambiar estado del libro a no disponible
            biblioteca["libros"][codigo_libro]["disponible"] = False
        # Crear diccionario del préstamo
            prestamo = {
        # Código del usuario
                "usuario": codigo_usuario,
        # Código del libro
                "libro": codigo_libro,
        # Fecha en que se prestó
                "fecha_prestamo": fecha_prestamo,
        # Fecha estimada de entrega
                "fecha_entrega": fecha_entrega,
        # Estado del préstamo
        # False significa que NO ha sido devuelto
                "devuelto": False
            }
        # Agregar préstamo a la lista de préstamos
        # append agrega elementos a una lista
            biblioteca["prestamos"].append(prestamo)
            print("✅ Libro prestado")

    # ======================================================
    # 7. DEVOLVER LIBRO
    # ======================================================

    elif opcion == 7:
        # Solicitar código del libro
        codigo_libro = input("Código del libro: ")       
        # Validar si el libro existe
        if codigo_libro not in biblioteca["libros"]:
            print("❌ Libro no existe")
        # Validar si el libro realmente está prestado
        elif biblioteca["libros"][codigo_libro]["disponible"] == True:
            print("❌ El libro no está prestado")
        else:  
        # Cambiar estado del libro a disponible
        
            biblioteca["libros"][codigo_libro]["disponible"] = True

        # Recorrer lista de préstamos
            for prestamo in biblioteca["prestamos"]:   
        # Buscar préstamo activo del libro
                if prestamo["libro"] == codigo_libro and prestamo["devuelto"] == False:                   
        # Cambiar estado del préstamo a devuelto
                    prestamo["devuelto"] = True          
        # break detiene el ciclo
                    break

            print("✅ Libro devuelto")

    # ======================================================
    # 8. MOSTRAR PRÉSTAMOS ACTIVOS
    # ======================================================
    elif opcion == 8:
        print("\n===== PRÉSTAMOS ACTIVOS =====")
        # Recorrer todos los préstamos
        for prestamo in biblioteca["prestamos"]:       
        # Mostrar solo préstamos no devueltos
            if prestamo["devuelto"] == False:
                print("\nUsuario:", prestamo["usuario"])
                print("Libro:", prestamo["libro"])
                print("Fecha préstamo:", prestamo["fecha_prestamo"])
                print("Fecha entrega:", prestamo["fecha_entrega"])

    # ======================================================
    # 9. MOSTRAR HISTORIAL
    # ======================================================

    elif opcion == 9:
        print("\n===== HISTORIAL =====") 
        # Recorrer todos los préstamos
        for prestamo in biblioteca["prestamos"]:     
        # Estado inicial
            estado = "Devuelto"         
        # Si aún no se devuelve cambia a Activo
            if prestamo["devuelto"] == False:
                estado = "Activo"  
        # Mostrar información del préstamo
            print("\nUsuario:", prestamo["usuario"])
            print("Libro:", prestamo["libro"])
            print("Fecha préstamo:", prestamo["fecha_prestamo"])
            print("Fecha entrega:", prestamo["fecha_entrega"])
            print("Estado:", estado)

    # ======================================================
    # 10. SALIR
    # ======================================================
    elif opcion == 10:
        # Mensaje de salida
        print("👋 Saliendo del sistema...")

    # ======================================================
    # OPCIÓN INVÁLIDA
    # ======================================================

    else:
        # Mensaje si la opción no existe
        print("❌ Opción inválida")