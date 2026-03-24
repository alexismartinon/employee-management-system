class LimiteDeFaltasExcedido(Exception):
    def __init__(self, mensaje="El empleado ha excedido el límite de faltas permitido."):
        self.mensaje = mensaje
        super().__init__(self.mensaje)


class EmpleadoNoDisponible(Exception):
    def __init__(self, mensaje="El empleado no está disponible para trabajar."):
        self.mensaje = mensaje
        super().__init__(self.mensaje)


class EmpleadoNoEncontrado(Exception):
    def __init__(self, mensaje="El empleado no fue encontrado en la base de datos."):
        self.mensaje = mensaje
        super().__init__(self.mensaje)
