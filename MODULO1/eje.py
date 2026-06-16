

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

veterinario = Veterinario("jose", "999", "Cirugia")
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