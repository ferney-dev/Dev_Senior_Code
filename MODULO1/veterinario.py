"""
 Ejercicio grupal: Sistema de gestión de hospital veterinario
Contexto
Una clínica veterinaria quiere desarrollar un sistema orientado a objetos para organizar 
su funcionamiento diario. El sistema debe permitir gestionar personas, mascotas, consultas, 
tratamientos, pagos y hospitalizaciones.Los estudiantes deben analizar el problema, identificar 
las clases, construir el modelo UML y luego implementar una versión funcional en Python.

Objetivo del ejercicio

Diseñar e implementar un sistema en Python que permita modelar el funcionamiento
básico de un hospital veterinario, aplicando correctamente relaciones entre clases y
principios de POO.

Lo que debe incluir obligatoriamente
1. Clase abstracta

Debe existir una clase abstracta llamada Persona.

De ella deben heredar otras clases.

Atributos sugeridos:
nombre
documento
Método abstracto obligatorio:
mostrar_rol()
2. Herencia

Desde Persona deben heredar al menos estas clases:

Veterinario
Recepcionista
Cliente

Cada una debe implementar mostrar_rol() de forma diferente.

3. Asociación

Debe existir una relación de asociación entre:

Veterinario y Mascota

porque un veterinario puede atender muchas mascotas y una mascota puede 
ser atendida por distintos veterinarios en diferentes momentos.

Esa relación puede reflejarse en la clase Consulta, donde se conectan ambas clases.

4. Agregación

Debe existir una relación de agregación entre:

Cliente y Mascota

porque un cliente tiene mascotas, pero la mascota puede seguir existiendo aunque 
el cliente se elimine del sistema.

El cliente debe tener un atributo como:

mascotas = []

y un método:

agregar_mascota()
5. Composición

Debe existir una relación de composición entre:

Consulta y Tratamiento

porque una consulta crea sus tratamientos como parte de sí misma.

La idea es que el tratamiento nazca dentro de la consulta.

La clase Consulta puede tener:

lista de tratamientos
método crear_tratamiento()
6. Polimorfismo

Debe existir una clase abstracta llamada MetodoPago.

De ella deben heredar:

PagoEfectivo
PagoTarjeta
PagoTransferencia

Cada una debe implementar el método:

procesar_pago(monto)

Luego una clase Factura debe usar cualquier objeto de tipo MetodoPago para cobrar una consulta.

Clases mínimas sugeridas

Los estudiantes deben trabajar, como mínimo, con estas clases:

Persona (abstracta)
Veterinario
Recepcionista
Cliente
Mascota
Consulta
Tratamiento
Factura
MetodoPago (abstracta)
PagoEfectivo
PagoTarjeta
PagoTransferencia
Reglas del sistema
Persona

Clase abstracta.

Atributos:
nombre
documento
Método abstracto:
mostrar_rol()
Veterinario

Hereda de Persona.

Atributos:
especialidad
Métodos:
mostrar_rol()
atender_mascota()
Recepcionista

Hereda de Persona.

Métodos:
mostrar_rol()
registrar_cliente()
Cliente

Hereda de Persona.

Atributos:
telefono
lista de mascotas
Métodos:
mostrar_rol()
agregar_mascota()
mostrar_mascotas()
Mascota
Atributos:
nombre
especie
edad
peso
Métodos:
mostrar_info()
Consulta
Atributos:
mascota
veterinario
motivo
diagnostico
tratamientos
Métodos:
crear_tratamiento()
mostrar_resumen()
calcular_costo_consulta()

Aquí se evidencia:

asociación con Mascota
asociación con Veterinario
composición con Tratamiento
Tratamiento
Atributos:
nombre
costo
duracion_dias
Métodos:
mostrar_tratamiento()
MetodoPago

Clase abstracta.

Método abstracto:
procesar_pago(monto)
PagoEfectivo

Hereda de MetodoPago.

PagoTarjeta

Hereda de MetodoPago.

PagoTransferencia

Hereda de MetodoPago.

Cada una debe implementar procesar_pago() de forma distinta.

Factura
Atributos:
consulta
subtotal
impuesto
total
Métodos:
calcular_total()
pagar(metodo_pago)

Aquí se debe aplicar polimorfismo.
[5:11 p. m., 13/4/2026] +57 302 2333949: Tareas del grupo
Parte 1. Análisis y modelado

Antes de programar, cada grupo debe:

Identificar las clases
Identificar atributos y métodos
Dibujar el diagrama UML a mano o digital
Marcar claramente:
herencia
agregación
composición
asociación
polimorfismo
Parte 2. Implementación en Python

Deben programar el sistema con las clases y relaciones solicitadas.

El código debe permitir como mínimo:

crear un cliente
agregar una o más mascotas al cliente
crear un veterinario
registrar una consulta para una mascota
crear uno o más tratamientos dentro de la consulta
generar una factura
pagar la factura con distintos métodos de pago
Parte 3. Prueba del sistema

Cada grupo debe mostrar una ejecución donde ocurra lo siguiente:

Se crea un cliente
Se registran dos mascotas
Un veterinario atiende una de las mascotas
Se crea una consulta
La consulta genera dos tratamientos
Se calcula el costo total
Se paga con un método de pago
Luego se cambia el método de pago y se prueba nuevamente
Entregables esperados

Cada grupo debe entregar:

diagrama UML
código Python funcional
una ejecución de prueba
explicación oral breve de dónde se ve cada concepto de POO
"""


from abc import ABC, abstractmethod


#CLASE ABSTRACTA PERSONA
class Persona(ABC):
    def __init__(self, nombre, documento):
        self.nombre = nombre
        self.documento = documento

    @abstractmethod
    def mostrar_rol(self):
        pass

#VETERINARIO
class Veterinario(Persona):
    def __init__(self, nombre, documento, especialidad):
        super().__init__(nombre, documento)
        self.especialidad = especialidad

    def mostrar_rol(self):
        print("Soy veterinario")
        print("Nombre:", self.nombre)
        print("Documento:", self.documento)
        print("Especialidad:", self.especialidad)
        print("******************************************")

    def atender_mascota(self, mascota):
        print("Atendiendo a:", mascota.nombre)
        print("******************************************")



#RECEPCIONISTA
class Recepcionista(Persona):
    def mostrar_rol(self):
        print("Soy recepcionista")
        print("******************************************")

    def registrar_cliente(self, cliente):
        print("Cliente registrado:", cliente.nombre)
        print("******************************************")



#CLIENTE
class Cliente(Persona):
    def __init__(self, nombre, documento, telefono):
        super().__init__(nombre, documento)
        self.telefono = telefono
        self.mascotas = []

    def mostrar_rol(self):
        print("Soy cliente")
        print("Nombre:", self.nombre)
        print("Documento:", self.documento)
        print("Teléfono:", self.telefono)
        print("******************************************")

    def agregar_mascota(self, mascota):
        self.mascotas.append(mascota)

    def mostrar_mascotas(self):
        print("Mascotas del cliente:")
        for m in self.mascotas:
            print("-", m.nombre)
        print("******************************************")

#MASCOTA
class Mascota:
    def __init__(self, nombre, especie, edad, peso):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        self.peso = peso

    def mostrar_info(self):
        print("\nInformación de la mascota")
        print("Nombre :", self.nombre)
        print("Especie:", self.especie)
        print("Edad   :", self.edad, "años")
        print("Peso   :", self.peso, "kg")
        print("******************************************")



#TRATAMIENTO
class Tratamiento:
    def __init__(self, nombre, costo, duracion_dias):
        self.nombre = nombre
        self.costo = costo
        self.duracion_dias = duracion_dias

    def mostrar_tratamiento(self):
        print("-", self.nombre, "| Costo:", self.costo)



#CONSULTA
class Consulta:
    def __init__(self, mascota, veterinario, motivo, diagnostico="Pendiente"):
        self.mascota = mascota
        self.veterinario = veterinario
        self.motivo = motivo
        self.diagnostico = diagnostico
        self.tratamientos = []

    def crear_tratamiento(self, nombre, costo, dias):
        t = Tratamiento(nombre, costo, dias)
        self.tratamientos.append(t)

    def calcular_costo_consulta(self):
        total = 0
        for t in self.tratamientos:
            total += t.costo
        return total

    def mostrar_resumen(self):
        print("\nResumen de la consulta")
        print("Mascota     :", self.mascota.nombre)
        print("Veterinario :", self.veterinario.nombre)
        print("Motivo      :", self.motivo)
        print("Diagnóstico :", self.diagnostico)

        print("Tratamientos:")
        for t in self.tratamientos:
            t.mostrar_tratamiento()

        print("Total:", self.calcular_costo_consulta())
        print("******************************************")



#METODO DE PAGO
class MetodoPago(ABC):
    @abstractmethod
    def procesar_pago(self, monto):
        pass

#PAGO EFECTIVO
class PagoEfectivo(MetodoPago):
    def procesar_pago(self, monto):
        print("Pago en efectivo:", monto)
        print("******************************************")

#PAGO TARJETA
class PagoTarjeta(MetodoPago):
    def procesar_pago(self, monto):
        print("Pago con tarjeta:", monto)
        print("******************************************")

#PAGO TRANSFERENCIA
class PagoTransferencia(MetodoPago):
    def procesar_pago(self, monto):
        print("Pago transferencia:", monto)
        print("******************************************")

#FACTURA 
class Factura:
    def __init__(self, consulta):
        self.consulta = consulta

    def calcular_total(self):
        subtotal = self.consulta.calcular_costo_consulta()
        return subtotal + (subtotal * 0.19)


    def mostrar_factura(self):
        print("\nFACTURA")
        print("Mascota:", self.consulta.mascota.nombre)
        print("Veterinario:", self.consulta.veterinario.nombre)
        print("Subtotal:", self.consulta.calcular_costo_consulta())
        print("Total con IVA:", self.calcular_total())
        print("******************************************")

    def pagar(self, metodo_pago):
        total = self.calcular_total()
        metodo_pago.procesar_pago(total)


cliente = Cliente("Ferney", "1055929332", "312082933")
cliente.mostrar_rol()

mascota1 = Mascota("Elena", "Gata", 3, 10)
mascota2 = Mascota("Tom", "Perro", 2, 5)

cliente.agregar_mascota(mascota1)
cliente.agregar_mascota(mascota2)

cliente.mostrar_mascotas()

mascota1.mostrar_info()
mascota2.mostrar_info()

veterinario = Veterinario("Carlos", "999", "Cirugia")
veterinario.mostrar_rol()

consulta = Consulta(mascota1, veterinario, "Dolor")
veterinario.atender_mascota(mascota1)

consulta.crear_tratamiento("Vacuna", 50000, 1)
consulta.crear_tratamiento("Medicamento", 30000, 5)

consulta.mostrar_resumen()

factura = Factura(consulta)
factura.mostrar_factura()

pago1 = PagoEfectivo()
factura.pagar(pago1)

pago2 = PagoTarjeta()
factura.pagar(pago2)