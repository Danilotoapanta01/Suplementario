# Nombre: Danilo Toapanta
# Universidad: Universidad Técnica Particular de Loja (UTPL)

# PASO 1: Se define la clase base Empleado
class Empleado:
    def __init__(self, nombre, salario_base):
        self.nombre = nombre
        self.salario_base = salario_base
    def calcular_salario(self):
        return self.salario_base
# PASO 2: Se crean las clases hijas usando herencia
class EmpleadoTiempoCompleto(Empleado):
    def __init__(self, nombre, salario_base, bono):
        super().__init__(nombre, salario_base)
        self.bono = bono
    def calcular_salario(self):
        return self.salario_base + self.bono
class EmpleadoMedioTiempo(Empleado):
    def __init__(self, nombre, horas_trabajadas, tarifa_hora):
        super().__init__(nombre, 0)
        self.horas_trabajadas = horas_trabajadas
        self.tarifa_hora = tarifa_hora
    def calcular_salario(self):
        return self.horas_trabajadas * self.tarifa_hora


# PASO 3: Se prueba el funcionamiento aplicando polimorfismo
if __name__ == "__main__":
    empleado1 = EmpleadoTiempoCompleto("Danilo Topanta", 60000, 1450)
    empleado2 = EmpleadoMedioTiempo("Barbara Flores", 86, 7)
    empleados = [empleado1, empleado2]
    for empleado in empleados:
        print(f"Empleado: {empleado.nombre}")
        print(f"Salario total: ${empleado.calcular_salario()}")
        print("----------------------------")
