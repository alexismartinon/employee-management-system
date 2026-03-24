from Exceptions import EmpleadoNoEncontrado


class Empresas:
    def __init__(self, empleados):
        self.empleados = empleados

    def buscar_empleado(self, id_empleado):
        for emp in self.empleados:
            if emp.id_empleado == id_empleado:
                return emp
        raise EmpleadoNoEncontrado(
            f"El empleado no fue encontrado en la base de datos.{id_empleado}")


class Trabajador:
    def __init__(self, id_empleado, nombre, apellido, edad, salario,  disponibilidad=True):
        self.id_empleado = id_empleado
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.salario = salario
        self.disponibilidad = disponibilidad
        self.__faltas = 0

    def __str__(self):
        return f"{self.nombre} {self.apellido}, Edad: {self.edad}, Salario: {self.salario}, Disponibilidad: {self.disponibilidad}"

    def asistio(self):
        if self.disponibilidad:
            self.disponibilidad = True
            return f"{self.nombre} {self.apellido} ha asistido al trabajo."

    def falto(self):
        if self.disponibilidad:
            self.disponibilidad = False
            self.__faltas += 1
            return f"{self.nombre} {self.apellido} ha faltado al trabajo. Total de faltas: {self.__faltas}"

    def trabajador_no_disponible(self):
        if not self.disponibilidad:
            raise ValueError(
                f"{self.nombre} {self.apellido} no está disponible para trabajar.")
        return True

    def to_dict(self):
        return {
            "id_empleado": self.id_empleado,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "edad": self.edad,
            "salario": self.salario,
            "disponibilidad": self.disponibilidad,
            "faltas": self.__faltas
        }
