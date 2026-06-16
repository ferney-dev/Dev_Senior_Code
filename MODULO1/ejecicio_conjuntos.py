"""1️⃣ Agregar un cliente
Solicitar:
Nombre del cliente
Teléfono
Crear el cliente con un diccionario vacío de mascotas
2️⃣ Agregar una mascota a un cliente
Solicitar:
Nombre del cliente
Nombre de la mascota
Especie
Edad
Peso
Guardar la mascota dentro del cliente
3️⃣ Mostrar todos los clientes y sus mascotas

Debe mostrar algo como:

Cliente: Carlos
 Teléfono: 123456
 Mascotas:
   - Firulais | Perro | 5 años | 12.5 kg
4️⃣ Buscar una mascota
Solicitar el nombre del cliente y la mascota
Mostrar toda la información de la mascota
5️⃣ Calcular el peso promedio de las mascotas de un cliente
Recorrer el diccionario anidado
Calcular el promedio del peso de todas las mascotas del cliente
6️⃣ Encontrar la mascota más pesada de toda la veterinaria
Debes recorrer todos los clientes y todas sus mascotas
7️⃣ Eliminar una mascota
Solicitar cliente y nombre de la mascota
Eliminarla del diccionario
8️⃣ Eliminar un cliente
Eliminar completamente su registro
🧩 Bonus (opcional 🔥)
Mostrar cuántas mascotas tiene cada cliente
Validar que no se repitan nombres de mascotas dentro del mismo cliente
Mostrar el cliente con más mascotas"""

clientes = {}
opcion = 0

menu = """MENU PRINCIPAL
1. Agregar un cliente
2. Agregar una mascota a un cliente
3. Mostrar todos los clientes y sus mascotas
4. Buscar una mascota
5. Calcular el peso promedio de las mascotas de un cliente
6. Encontrar la mascota más pesada de toda la veterinaria
7. Eliminar una mascota
8. Eliminar un cliente
9. Salir
"""
while opcion != 9:
    print(menu)
    opcion = int(input("Seleccione una opcion: "))

    if opcion == 1:
        nombre_cliente = input("Ingrese el nombre del cliente: ")
        telefono = input("Ingrese el teléfono del cliente: ")
        if nombre_cliente in clientes:
            print("El cliente ya existe.")
        else:
            clientes[nombre_cliente] = {"telefono": telefono, "mascotas": []}
            print(f"Cliente {nombre_cliente} agregado exitosamente.")
            print(clientes)   
    elif opcion == 2:
        nombre_cliente = input("Ingrese el nombre del cliente: ")
        if nombre_cliente in clientes:
            nombre_mascota = input("Ingrese el nombre de la mascota: ")
            especie = input("Ingrese la especie de la mascota: ")
            edad = input("Ingrese la edad de la mascota: ")
            peso = float(input("Ingrese el peso de la mascota: "))
            mascota = {"nombre": nombre_mascota, "especie": especie, "edad": edad, "peso": peso}
            clientes[nombre_cliente]["mascotas"].append(mascota)
            print(f"Mascota {nombre_mascota} agregada a {nombre_cliente}.")
        else:
            print("El cliente no existe.")
        print(clientes)
    elif opcion == 3:
        if len(clientes) == 0:
            print("No hay clientes registrados.")
        else:
            for nombre_cliente, info in clientes.items():
                print(f"Cliente: {nombre_cliente}")
                print(f" Teléfono: {info['telefono']}")
                print(" Mascotas:")
                for mascota in info["mascotas"]:
                    print(f"   - {mascota['nombre']} | {mascota['especie']} | {mascota['edad']} años | {mascota['peso']} kg")
    elif opcion == 4:
        nombre_cliente = input("Ingrese el nombre del cliente: ")
        if nombre_cliente in clientes:
            nombre_mascota = input("Ingrese el nombre de la mascota: ")
            mascota_encontrada = None
            for mascota in clientes[nombre_cliente]["mascotas"]:
                if mascota["nombre"] == nombre_mascota:
                    mascota_encontrada = mascota
                    break
            if mascota_encontrada:
                print(f"Información de la mascota {nombre_mascota}:")
                print(f" Especie: {mascota_encontrada['especie']}")
                print(f" Edad: {mascota_encontrada['edad']} años")
                print(f" Peso: {mascota_encontrada['peso']} kg")
            else:
                print("La mascota no existe.")
        else:
            print("El cliente no existe.")
    elif opcion == 5:
        nombre_cliente = input("Ingrese el nombre del cliente: ")
        if nombre_cliente in clientes:
            mascotas = clientes[nombre_cliente]["mascotas"]
            if len(mascotas) > 0:
                peso_total = sum(mascota["peso"] for mascota in mascotas)
                promedio_peso = peso_total / len(mascotas)
                print(f"El peso promedio de las mascotas de {nombre_cliente} es: {promedio_peso:.2f} kg.")
            else:
                print(f"{nombre_cliente} no tiene mascotas registradas.")
        else:
            print("El cliente no existe.")
    elif opcion == 6:
        mascota_mas_pesada = None
        peso_maximo = -1
        for info in clientes.values():
            for mascota in info["mascotas"]:
                if mascota["peso"] > peso_maximo:
                    peso_maximo = mascota["peso"]
                    mascota_mas_pesada = mascota
        if mascota_mas_pesada:
            print(f"La mascota más pesada es {mascota_mas_pesada['nombre']} con un peso de {peso_maximo:.2f} kg.")
        else:
            print("No hay mascotas registradas.")
    elif opcion == 7:
        nombre_cliente = input("Ingrese el nombre del cliente: ")
        if nombre_cliente in clientes:
            nombre_mascota = input("Ingrese el nombre de la mascota a eliminar: ")
            mascotas = clientes[nombre_cliente]["mascotas"]
            mascota_eliminada = False
            for i, mascota in enumerate(mascotas):
                if mascota["nombre"] == nombre_mascota:
                    del mascotas[i]
                    mascota_eliminada = True
                    print(f"Mascota {nombre_mascota} eliminada de {nombre_cliente}.")
                    break
            if not mascota_eliminada:
                print("La mascota no existe.")
        else:
            print("El cliente no existe.")
    elif opcion == 8:
        nombre_cliente = input("Ingrese el nombre del cliente a eliminar: ")
        if nombre_cliente in clientes:
            del clientes[nombre_cliente]
            print(f"Cliente {nombre_cliente} eliminado exitosamente.")
        else:
            print("El cliente no existe.")
    elif opcion == 9:
        print("Saliendo del programa. ¡Hasta luego!")


