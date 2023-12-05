
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
        localizacion = input("Localización: ")
        departamento = input("Departamento: ")
        cargo = input("Cargo: ")
        solicitud = f"insert {nombre} {pais} {ciudad} {localizacion} {departamento} {cargo}"
        enviar_solicitud(solicitud)
    
    elif opcion == '5':
        break