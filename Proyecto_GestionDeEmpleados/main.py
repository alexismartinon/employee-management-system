from Persona import empleadosfalto, empleadosasistio
from Empresa import Empresas
from Exceptions import EmpleadoNoEncontrado
from Empresa import Empresas, Trabajador


print("Bienvenido al sistema de gestión de empleados")

while True:

    menu = int(input(
        "Que deseas hacer? \n1. Ver empleados que faltaron \n2. Ver empleados que asistieron \n3. Salir \n4 Acceso ROOT\n"))
    try:
        if menu == 1:
            print("Empleados que faltaron: ")
            for emp in empleadosfalto:
                print(emp)
        elif menu == 2:
            print("Empleados que asistieron: ")
            for emp in empleadosasistio:
                print(emp)
        elif menu == 3:
            print("Saliendo del sistema...")
            break
        elif menu == 4:
            privilegio = input(
                "Ingrese la contraseña para acceder a privilegios especiales: ")
            if privilegio != "admin123":
                print("Contraseña incorrecta. Acceso denegado.")
                break
            print("Accediendo a privilegios especiales...")
            orden = int(input(
                "Seleccione una opción: \n1. Buscar empleado por ID Y Ver todos los empleados \n2. Salario Actualizado \n3. Faltas Actualizadas \n4. Agregar empleado \n5 Eliminar empleado \n6. Salir \n"))
            if orden == 1:
                # unir todos los empleados
                todos = empleadosfalto + empleadosasistio
                # crear empresa
                empresa = Empresas(todos)
                # pedir ID
                buscador = int(
                    input("Ingrese el ID del empleado que desea buscar: "))
                empleado = empresa.buscar_empleado(buscador)
                print(f"Empleado encontrado: {empleado}")
                # convertir listas a diccionarios
                empleadosfalto_dict = [emp.to_dict() for emp in empleadosfalto]
                empleadosasistio_dict = [emp.to_dict()
                                         for emp in empleadosasistio]
                print("Faltaron:")
                for e in empleadosfalto_dict:
                    print(e)

                print("\nAsistieron:")
                for e in empleadosasistio_dict:
                    print(e)
            elif orden == 2:
                print("Funcionalidad de salario aún no implementada.")
                break
            elif orden == 3:
                print("Funcionalidad de faltas aún no implementada.")
                break
            elif orden == 4:
                print("Funcionalidad de agregar empleado aún no implementada.")
                break
            elif orden == 5:
                print("Funcionalidad de eliminar empleado aún no implementada.")
                break
            elif orden == 6:
                print("Saliendo del sistema...")
                break
    except EmpleadoNoEncontrado as e:
        print(e)
