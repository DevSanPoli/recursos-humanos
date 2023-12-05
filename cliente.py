import os


def enviar_solicitud(solicitud):
    pass

while True:
    print("Opciones:")
    print("1. Insertar empleado")
    print("2. Consultar empleado")
    print("3. Marcar empleado como borrado")
    print("4. Actualizar dirección y ciudad del empleado")
    print("5. Salir")
    
    opcion = input("Selecciona una opción: ")
    
    if opcion == '1':

        nombre = input("Nombre del empleado: ")
        pais = input("País: ")
        ciudad = input("Ciudad: ")
        direccion = input("Dirección: ")
        departamento = input("Departamento: ")
        cargo = input("Cargo: ")
        cc =  input("Identificación:")

        insertar = {
            'nombre': nombre,
            'pais': pais,
            'ciudad': ciudad,
            'direccion': direccion,
            'departamento': departamento,
            'cargo': cargo,
            'cc': cc
        }

        enviar_solicitud(insertar)

        os.system('clear')
    
    if opcion == '2':
        identificacion = input("Escriba la identeficición del empleado a consultar: ")

        enviar_solicitud(identificacion)
        os.system('clear')

    if opcion == '3':
        identificacion = input("Escriba la identificición del empleado a eliminar: ")

        enviar_solicitud(identificacion)
        os.system('clear')
    
    if opcion == '4':
        identificacion = input("Escriba la identificición del empleado a modificar: ")
        ciudad = input("Digite la nueva ciudad del empleado: ")
        direccion = input("Digite la nueva dirección del empleado: ß")


        enviar_solicitud(identificacion)
        os.system('clear')

    
    elif opcion == '5':
        break