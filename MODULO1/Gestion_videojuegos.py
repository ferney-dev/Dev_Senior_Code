"""
Ejercicio Integrador en Python
Sistema de Gestión de una Tienda de Videojuegos
Objetivo
Desarrollar un programa en Python que permita administrar el inventario y las ventas de una tienda de videojuegos utilizando:
Variables
Condicionales (if, elif, else)
Ciclos (while, for)
Funciones
Colecciones (diccionarios y listas)


Enunciado del Problema
Una tienda de videojuegos desea llevar el control de sus productos y ventas.
Cada videojuego tendrá la siguiente información:
Código
Nombre
Plataforma (PC, PlayStation, Xbox, Nintendo)
Precio
Cantidad en inventario
La información se almacenará en un diccionario con la siguiente estructura:
Python


videojuegos = {
    "VG001": {
        "nombre": "FIFA 26",
        "plataforma": "PlayStation 5",
        "precio": 250000,
        "cantidad": 10
    }
}


Menú Principal
El programa debe mostrar repetidamente el siguiente menú:
Plain text
===== TIENDA DE VIDEOJUEGOS =====
1. Agregar videojuego
2. Mostrar inventario
3. Buscar videojuego por código
4. Actualizar precio
5. Registrar venta
6. Mostrar estadísticas
7. Eliminar videojuego
8. Salir


Requisitos del Programa
1. Agregar videojuego
Crear una función que solicite los datos del videojuego y lo agregue al diccionario.
Validaciones:
No se debe permitir un código repetido.
El precio y la cantidad deben ser mayores que cero.
2. Mostrar inventario
Recorrer el diccionario e imprimir todos los videojuegos registrados.
3. Buscar videojuego por código
Solicitar un código y mostrar toda la información del videojuego si existe.
4. Actualizar precio
Permitir cambiar el precio de un videojuego existente.
5. Registrar venta
Solicitar:
Código del videojuego
Cantidad a vender
Validaciones:
El videojuego debe existir.
Debe haber suficiente inventario.
Acciones:
Restar del inventario.
Calcular el valor total de la venta.
Mostrar factura.
6. Mostrar estadísticas
Crear una función que muestre:
Total de videojuegos registrados.
Valor total del inventario.
Videojuego más costoso.
Videojuego con mayor cantidad disponible.
Promedio de precios.
7. Eliminar videojuego
Eliminar un videojuego por código.
8. Salir
Finalizar el programa.
Requisitos Técnicos
Funciones obligatorias
Debes implementar al menos las siguientes funciones:
Python


def agregar_videojuego(videojuegos):
def mostrar_inventario(videojuegos):
def buscar_videojuego(videojuegos):
def actualizar_precio(videojuegos):
def registrar_venta(videojuegos):
def mostrar_estadisticas(videojuegos):
def eliminar_videojuego(videojuegos):
def menu():
    
    
Datos Iniciales de Prueba
Python
videojuegos = {
    "VG001": {
        "nombre": "FIFA 26",
        "plataforma": "PlayStation 5",
        "precio": 250000,
        "cantidad": 10
    },
    "VG002": {
        "nombre": "Zelda: Breath of the Wild",
        "plataforma": "Nintendo Switch",
        "precio": 220000,
        "cantidad": 5
    },
    "VG003": {
        "nombre": "Forza Horizon 5",
        "plataforma": "Xbox Series X",
        "precio": 210000,
        "cantidad": 8
    }
}


Ejemplo de Venta
Plain text
Ingrese código del videojuego: VG001
Ingrese cantidad a vender: 2

Factura:
Juego: FIFA 26
Precio unitario: $250000
Cantidad: 2
Total: $500000
Retos Adicionales (Opcionales)
Si terminas antes, agrega:
Buscar videojuegos por plataforma.
Mostrar videojuegos con inventario bajo (cantidad < 3).
Aplicar descuentos del 10% en ventas mayores a $500.000.
Guardar historial de ventas en una lista.
Mostrar el videojuego más vendido.
Conceptos que Practicarás
Diccionarios anidados
Listas
Funciones con parámetros y retorno
Condicionales
Ciclos while y for
Validación de datos
Cálculos estadísticos básicos
Nivel de Dificultad
Intermedio
Tiempo Estimado
2 a 3 horas
Resultado Esperado
Al finalizar tendrás un sistema completo de consola para administrar una tienda de videojuegos, aplicando de 
forma práctica los principales fundamentos de Python.
"""


# PROYECTO FINAL - MoDULO 3
# SISTEMA DE GESTIoN DE TIENDA DE VIDEOJUEGOS
# DICCIONARIO PRINCIPAL DEL INVENTARIO

videojuegos = {

    "VG001": {
        "nombre": "FIFA 26",
        "plataforma": "PlayStation 5",
        "precio": 250000,
        "cantidad": 10
    },

    "VG002": {
        "nombre": "Zelda: Breath of the Wild",
        "plataforma": "Nintendo Switch",
        "precio": 220000,
        "cantidad": 5
    },

    "VG003": {
        "nombre": "Forza Horizon 5",
        "plataforma": "Xbox Series X",
        "precio": 210000,
        "cantidad": 8
    }
}

# LISTA PARA GUARDAR HISTORIAL DE VENTAS
historial_ventas = []



# FUNCIoN PARA VALIDAR NÚMEROS
def validar_numero(numero):
    if numero.replace(".", "", 1).isdigit():
        return True
    else:
        return False

# FUNCIoN: AGREGAR VIDEOJUEGO
def agregar_videojuego(videojuegos):
    print("\n-------- AGREGAR VIDEOJUEGO --------")
    codigo = input("Ingrese el codigo del videojuego: ").upper()

    if codigo == "":
        print("El codigo no puede estar vacio")
        return

    if codigo in videojuegos:
        print("El codigo ya existe")
        return

    nombre = input("Ingrese el nombre del videojuego: ")
    
    if nombre == "":
        print("El nombre no puede estar vacio")
        return

    plataforma = input("Ingrese la plataforma: ")
    
    if plataforma == "":
        print("La plataforma no puede estar vacia")
        return

    precio = input("Ingrese el precio: ")
    
    if validar_numero(precio) == False:
        print("El precio debe ser numérico")
        return

    precio = float(precio)

    if precio <= 0:
        print("El precio debe ser mayor a 0")
        return

    cantidad = input("Ingrese la cantidad disponible: ")

    if cantidad.isdigit() == False:
        print("La cantidad debe ser numérica")
        return

    cantidad = int(cantidad)

    if cantidad < 0:
        print("La cantidad no puede ser negativa")
        return

    # Agregar videojuego al diccionario
    videojuegos[codigo] = {
        "nombre": nombre,
        "plataforma": plataforma,
        "precio": precio,
        "cantidad": cantidad
    }
    print("Videojuego agregado exitosamente")



# FUNCIoN: MOSTRAR INVENTARIO
def mostrar_inventario(videojuegos):
    print("\n--------- INVENTARIO DE VIDEOJUEGOS --------")

    if len(videojuegos) == 0:
        print("No hay videojuegos registrados")
        return

    print("-" * 95)
    print(f"{'CODIGO':<10} {'NOMBRE':<30} {'PLATAFORMA':<25} {'PRECIO':<12} {'STOCK':<10}")
    print("-" * 95)
    
    for codigo, datos in videojuegos.items():
        print(f"{codigo:<10} "
              f"{datos['nombre']:<30} "
              f"{datos['plataforma']:<25} "
              f"${datos['precio']:<10,.0f} "
              f"{datos['cantidad']:<10}")

    print("-" * 95)



# FUNCIoN: BUSCAR VIDEOJUEGO
def buscar_videojuego(videojuegos):

    print("\n----- BUSCAR VIDEOJUEGO -----")
    
    codigo = input("Ingrese el codigo del videojuego: ").upper()

    if codigo in videojuegos:
        juego = videojuegos[codigo]
        print("\n VIDEOJUEGO ENCONTRADO")
        print("-" * 40)
        print(f"Codigo: {codigo}")
        print(f"Nombre: {juego['nombre']}")
        print(f"Plataforma: {juego['plataforma']}")
        print(f"Precio: ${juego['precio']:,.0f}")
        print(f"Cantidad disponible: {juego['cantidad']}")
    else:
        print(" Videojuego no encontrado")



# FUNCIoN: ACTUALIZAR PRECIO
def actualizar_precio(videojuegos):

    print("\n-------- ACTUALIZAR PRECIO --------")
    
    codigo = input("Ingrese el codigo del videojuego: ").upper()

    if codigo not in videojuegos:
        print("El videojuego no existe")
        return

    nuevo_precio = input("Ingrese el nuevo precio: ")

    if validar_numero(nuevo_precio) == False:
        print("Debe ingresar un número válido")
        return

    nuevo_precio = float(nuevo_precio)

    if nuevo_precio <= 0:
        print("El precio debe ser mayor a 0")
        return

    videojuegos[codigo]["precio"] = nuevo_precio

    print(" Precio actualizado correctamente")


# FUNCIoN: REGISTRAR VENTA
def registrar_venta(videojuegos):

    print("\n------- REGISTRAR VENTA -------")

    codigo = input("Ingrese el codigo del videojuego: ").upper()

    if codigo not in videojuegos:
        print("El videojuego no existe")
        return

    juego = videojuegos[codigo]

    print(f"Stock disponible: {juego['cantidad']}")

    cantidad_vender = input("Ingrese cantidad a vender: ")

    if cantidad_vender.isdigit() == False:
        print("Debe ingresar números enteros")
        return

    cantidad_vender = int(cantidad_vender)

    if cantidad_vender <= 0:
        print("La cantidad debe ser mayor a 0")
        return

    if cantidad_vender > juego["cantidad"]:
        print("No hay suficiente stock")
        return

    subtotal = juego["precio"] * cantidad_vender

    descuento = 0

    if subtotal > 500000:

        descuento = subtotal * 0.10
        
    total = subtotal - descuento

    videojuegos[codigo]["cantidad"] -= cantidad_vender

    venta = {

        "codigo": codigo,
        "nombre": juego["nombre"],
        "cantidad": cantidad_vender,
        "total": total
    }

    historial_ventas.append(venta)

    print("\n------FACTURA DE VENTA------")
    print(f"Juego: {juego['nombre']}")
    print(f"Plataforma: {juego['plataforma']}")
    print(f"Precio unitario: ${juego['precio']:,.0f}")
    print(f"Cantidad vendida: {cantidad_vender}")
    print(f"Subtotal: ${subtotal:,.0f}")

    if descuento > 0:
        print(f"Descuento aplicado: ${descuento:,.0f}")

    print(f"TOTAL A PAGAR: ${total:,.0f}")

    print("=============================")

    print("Venta registrada exitosamente")

    if videojuegos[codigo]["cantidad"] < 3:
        print("ALERTA: Inventario bajo")



# FUNCIoN: MOSTRAR ESTADiSTICAS
def mostrar_estadisticas(videojuegos):

    print("\n------ ESTADiSTICAS DEL INVENTARIO ------")

    if len(videojuegos) == 0:
        print("No hay videojuegos registrados")
        return

    total_videojuegos = len(videojuegos)

    valor_total = 0
    suma_precios = 0

    juego_costoso = ""
    precio_mayor = 0

    juego_mayor_stock = ""
    mayor_stock = 0

    for codigo, datos in videojuegos.items():

        valor_total += datos["precio"] * datos["cantidad"]

        suma_precios += datos["precio"]

        if datos["precio"] > precio_mayor:

            precio_mayor = datos["precio"]
            juego_costoso = datos["nombre"]

        if datos["cantidad"] > mayor_stock:

            mayor_stock = datos["cantidad"]
            juego_mayor_stock = datos["nombre"]

    promedio_precios = suma_precios / total_videojuegos

    print("-" * 50)

    print(f"Total de videojuegos: {total_videojuegos}")

    print(f"Valor total del inventario: ${valor_total:,.0f}")

    print(f"Videojuego más costoso: {juego_costoso} (${precio_mayor:,.0f})")

    print(f"Mayor cantidad disponible: {juego_mayor_stock} ({mayor_stock} unidades)")

    print(f"Promedio de precios: ${promedio_precios:,.0f}")

    print("-" * 50)



# FUNCIoN: ELIMINAR VIDEOJUEGO
def eliminar_videojuego(videojuegos):

    print("\n----- ELIMINAR VIDEOJUEGO -----")

    codigo = input("Ingrese el codigo del videojuego: ").upper()

    if codigo not in videojuegos:
        print("El videojuego no existe")
        return

    print(f"Videojuego encontrado: {videojuegos[codigo]['nombre']}")

    confirmacion = input("¿Seguro que desea eliminarlo? (si/no): ").lower()

    if confirmacion == "si":

        del videojuegos[codigo]

        print("Videojuego eliminado correctamente")

    else:
        print("Eliminacion cancelada")


# FUNCIoN: MOSTRAR HISTORIAL DE VENTAS
def mostrar_historial_ventas():
    print("\n-------- HISTORIAL DE VENTAS --------")

    if len(historial_ventas) == 0:
        print("No hay ventas registradas")
        return

    for venta in historial_ventas:
        print("-" * 40)
        print(f"Codigo: {venta['codigo']}")
        print(f"Juego: {venta['nombre']}")
        print(f"Cantidad vendida: {venta['cantidad']}")
        print(f"Total pagado: ${venta['total']:,.0f}")

    print("-" * 40)



# FUNCIoN PRINCIPAL: MENU
def menu():

    while True:
        print("\n")
        print("------ TIENDA DE VIDEOJUEGOS ------")
        print("1. Agregar videojuego")
        print("2. Mostrar inventario")
        print("3. Buscar videojuego")
        print("4. Actualizar precio")
        print("5. Registrar venta")
        print("6. Mostrar estadisticas")
        print("7. Eliminar videojuego")
        print("8. Mostrar historial de ventas")
        print("9. Salir")

        opcion = input("Seleccione una opcion (1-9): ")

        if opcion == "1":

            agregar_videojuego(videojuegos)

        elif opcion == "2":

            mostrar_inventario(videojuegos)

        elif opcion == "3":

            buscar_videojuego(videojuegos)

        elif opcion == "4":

            actualizar_precio(videojuegos)

        elif opcion == "5":

            registrar_venta(videojuegos)

        elif opcion == "6":

            mostrar_estadisticas(videojuegos)

        elif opcion == "7":

            eliminar_videojuego(videojuegos)

        elif opcion == "8":

            mostrar_historial_ventas()

        elif opcion == "9":
            print("Programa finalizado")
            break

        else:
            print("Opcion inválida")


menu()