# Crear un sistema que permita:

# 1. Registrar productos con su nombre, precio y cantidad.
# 2. Mostrar inventario
# 3. Buscar productos
# 4. Validar datos
# 5. Guardar información en csv
# 6. Terminar

#la estructura sería:
# nombre, precio, cantidad
# Mause, 150, 10
# Teclado, 300, 5
# Monitor, 1200, 3

def registrar_producto(productos):
    pass

def mostrar_inventario(productos):   
    pass

def buscar_producto(productos):
    pass

def validar_datos(productos):
    pass

def guardar_en_csv(productos):
    pass

def cargar_productos_inisiales():
    productos [
        {"nombre": "Mause", "precio": 150, "cantidad": 10},
        {"nombre": "Teclado", "precio": 300, "cantidad": 5},
        {"nombre": "Monitor", "precio": 1200, "cantidad": 3}
    ]


def mostrar_menu():
    print("\n=== MENÚ ===")
    print("1. Registrar producto")
    print("2. Mostrar inventario")
    print("3. Buscar producto")
    print("4. Validar datos")
    print("5. Guardar informacion en CSV")
    print("6. Terminar")   
    
    def ejecutar_programa():
        productos = []
        
        opcion = 0
        
        while opcion != 6:
            mostrar_menu()
            try:
                opcion = int(input("Seleccione una opción: "))
                
                if opcion == 1:
                    registrar_producto(productos)
                elif opcion == 2:
                    mostrar_inventario(productos)
                elif opcion == 3:
                    buscar_producto(productos)
                elif opcion == 4:
                    validar_datos(productos)
                elif opcion == 5:
                    guardar_en_csv()
                elif opcion == 6:
                    print("Saliendo del programa...")
                else:
                    print("Opción no válida. Por favor, seleccione una opción del menú.")
            except ValueError:
                print("Error: Debe ingresar un número válido para seleccionar una opción.") 
                
    ejecutar_programa()