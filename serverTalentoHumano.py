import socket
import pyodbc
import json

# Configuración de la conexión a la base de datos SQL Server
server = '127.0.0.1'
database = 'ResursosHumanos'
username = 'desa'
password = '123'

db_connection = pyodbc.connect(
    f'DRIVER=SQL Server;SERVER={server};DATABASE={database};UID={username};PWD={password}')
cursor = db_connection.cursor()

# Configuración del servidor socket
host = '127.0.0.1'
port = 5555

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(1)

print(f"Servidor escuchando en {host}:{port}...")

while True:
    # Aceptar la conexión del cliente
    client_socket, client_address = server_socket.accept()
    print(f"Conexión establecida desde {client_address}")

    # Recibir la solicitud del cliente y decodificarla desde JSON
    data = client_socket.recv(1024).decode('utf-8')
    request = json.loads(data)

    # Procesar la solicitud del cliente
    if request["action"] == "select":
        # Consulta para seleccionar todos los empleados
        consulta = "SELECT * FROM empleado"
        resultado = cursor.execute(consulta).fetchall()

        # Recuperar las columnas del resultado
        columnas = [column[0] for column in cursor.description]

        # Recuperar todas las filas como diccionarios
        filas = [dict(zip(columnas, map(str, fila))) for fila in resultado]

        # Construir la respuesta con éxito y enviarla al cliente
        response = {"status": "success", "data": filas}

    elif request["action"] == "insert":
        # Consulta para insertar un nuevo empleado
        consulta = "INSERT INTO empleado (nombre, apellido, fecha_nacimiento, direccion, telefono, correo, id_departamento, id_profesion, id_cargo, fecha_ingreso, salario) VALUES (?,?,?,?,?,?,?,?,?,?,?)"
        cursor.execute(consulta, (request["nombre"], request["apellido"], request["fecha_nacimiento"], request["direccion"], request["telefono"],
                                  request["correo"], request["id_departamento"], request["id_profesion"], request["id_cargo"], request["fecha_ingreso"], request["salario"]))
        db_connection.commit()

        # Construir la respuesta con éxito y enviarla al cliente
        response = {"status": "success", "message": "Empleado insertado"}

    elif request["action"] == "update":
        # Consulta para actualizar la dirección y el teléfono de un empleado
        consulta = "UPDATE empleado SET direccion = ?, telefono = ? WHERE id_empleado = ?"
        cursor.execute(
            consulta, request["direccion"], request["telefono"], request["id"])
        db_connection.commit()

        # Construir la respuesta con éxito y enviarla al cliente
        response = {"status": "success", "message": "Empleado actualizado"}

    elif request["action"] == "delete":
        # Consulta para eliminar un empleado por su ID
        consulta = "DELETE FROM empleado WHERE id_empleado = ?"
        cursor.execute(consulta, (request["id"]))
        db_connection.commit()

        # Construir la respuesta con éxito y enviarla al cliente
        response = {"status": "success", "message": "Empleado eliminado"}

    elif request["action"] == "Departamento":
        # Consulta para obtener la información de los departamentos
        consulta = "SELECT * FROM departamento"
        resultado = cursor.execute(consulta).fetchall()

        # Recuperar las columnas del resultado
        columnas = [column[0] for column in cursor.description]

        # Recuperar todas las filas como diccionarios
        filas = [dict(zip(columnas, map(str, fila))) for fila in resultado]

        # Construir la respuesta con éxito y enviarla al cliente
        response = {"status": "success", "data": filas}

    elif request["action"] == "Profesion":
        # Consulta para obtener la información de las profesiones
        consulta = "SELECT * FROM profesion"
        resultado = cursor.execute(consulta).fetchall()

        # Recuperar las columnas del resultado
        columnas = [column[0] for column in cursor.description]

        # Recuperar todas las filas como diccionarios
        filas = [dict(zip(columnas, map(str, fila))) for fila in resultado]

        # Construir la respuesta con éxito y enviarla al cliente
        response = {"status": "success", "data": filas}

    elif request["action"] == "Cargo":
        # Consulta para obtener la información de los cargos
        consulta = "SELECT * FROM cargo"
        resultado = cursor.execute(consulta).fetchall()

        # Recuperar las columnas del resultado
        columnas = [column[0] for column in cursor.description]

        # Recuperar todas las filas como diccionarios
        filas = [dict(zip(columnas, map(str, fila))) for fila in resultado]

        # Construir la respuesta con éxito y enviarla al cliente
        response = {"status": "success", "data": filas}

    else:
        # Si la acción no es válida, construir una respuesta de error
        response = {"status": "error", "message": "Acción no válida"}

    # Enviar la respuesta al cliente
    client_socket.send(json.dumps(response).encode('utf-8'))

    # Cerrar la conexión con el cliente
    client_socket.close()
