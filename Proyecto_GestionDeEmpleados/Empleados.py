from Persona import empleadosasistio, empleadosfalto


class Nomina:
    def __init__(self, nombre, apellido, salario):
        self.nombre = nombre
        self.apellido = apellido
        self.salario = salario

    def salario_total(self, comision=500):
        return f"El salario total de {self.nombre} {self.apellido} es: {self.salario + comision}"
