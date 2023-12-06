import os
import socket
import json


"""
    Función para enviar solicitudes al servidor y recibir la respuesta.

    Args:
        solicitud (dict): Diccionario que contiene la solicitud.

    Returns:
        dict: Respuesta del servidor en formato de diccionario.
"""


def enviar_solicitud(solicitud):

    host = '127.0.0.1'
    port = 5555

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    client_socket.send(json.dumps(solicitud).encode('utf-8'))

    data = client_socket.recv(2048).decode('utf-8')
    response = json.loads(data)
    client_socket.close()
    return response


"""
    Función para obtener y mostrar relaciones específicas desde el servidor.

    Args:
        opcion (int): Opción que indica qué tipo de relación se está solicitando
                      (1 para Departamento, 2 para Profesión, 3 para Cargo).

    Prints:
        Muestra en consola las relaciones recuperadas desde el servidor.
"""


def relaciones(opcion):
    if opcion == 1:
        consulta = {
            'action': 'Departamento',

        }

        respuesta = enviar_solicitud(consulta)
        if respuesta["status"] == "success":
            for fila in respuesta["data"]:
                print(f" {fila}")
    elif opcion == 2:
        consulta = {
            'action': 'Profesion',

        }

        respuesta = enviar_solicitud(consulta)
        if respuesta["status"] == "success":
            for fila in respuesta["data"]:
                print(f" {fila}")

    elif opcion == 3:
        consulta = {
            'action': 'Cargo',

        }

        respuesta = enviar_solicitud(consulta)
        if respuesta["status"] == "success":
            for fila in respuesta["data"]:
                print(f" {fila}")


while True:
    # Menú principal del programa
    print("Opciones:")
    print("1. Insertar empleado")
    print("2. Consultar Todos los empleados")
    print("3. Actualizar dirección y ciudad del empleado")
    print("4. Eliminar empleado")
    print("5. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == '1':
        # Sección para insertar un nuevo empleado con relaciones.
        nombre = input("Nombre del empleado: ")
        apellido = input("Apellido del empleado: ")
        print("Formato de fecha: YYYY-MM-DD")
        fecha_nacimiento = input("Fecha de nacimiento: ")
        direccion = input("Dirección: ")
        telefono = input("Teléfono: ")
        correo = input("Correo: ")
        print("escoja el id del departamento")
        relaciones(1)
        id_departamento = input("Id del departamento: ")
        print("escoja el id de la profesión")
        relaciones(2)
        id_profesion = input("Id de la profesión: ")
        print("escoja el id del cargo")
        relaciones(3)
        id_cargo = input("Id del cargo: ")
        print("Formato de fecha: YYYY-MM-DD")
        fecha_ingreso = input("Fecha de ingreso: ")
        salario = input("Salario: ")
        insertar = {
            'action': 'insert',
            'nombre': nombre,
            'apellido': apellido,
            'fecha_nacimiento': fecha_nacimiento,
            'direccion': direccion,
            'telefono': telefono,
            'correo': correo,
            'id_departamento': id_departamento,
            'id_profesion': id_profesion,
            'id_cargo': id_cargo,
            'fecha_ingreso': fecha_ingreso,
            'salario': salario

        }

        respuesta = enviar_solicitud(insertar)
        if respuesta["status"] == "success":
            print(respuesta["message"])

    if opcion == '2':
        # Sección para consultar todos los empleados.
        consulta = {
            'action': 'select',


        }

        respuesta = enviar_solicitud(consulta)
        if respuesta["status"] == "success":
            for fila in respuesta["data"]:
                print(f" {fila}")

    if opcion == '4':
        # Sección para eliminar un empleado.
        identificacion = input(
            "Escriba el id  del empleado a eliminar: ")
        consulta = {
            'action': 'delete',
            'id': identificacion
        }

        respuesta = enviar_solicitud(consulta)
        if respuesta["status"] == "success":
            print(respuesta["message"])

    if opcion == '3':
        # Sección para actualizar dirección y teléfono de un empleado.
        identificacion = input(
            "Escriba la identificición del empleado a modificar: ")
        direccion = input("Digite la nueva direccion del empleado: ")
        telefono = input("Teléfono: ")

        consulta = {
            'action': 'update',
            'id': identificacion,
            'direccion': direccion,
            'telefono': telefono
        }

        respuesta = enviar_solicitud(consulta)
        if respuesta["status"] == "success":
            print(respuesta["message"])

    elif opcion == '5':
        # Salir del bucle si la opción es '5'
        break