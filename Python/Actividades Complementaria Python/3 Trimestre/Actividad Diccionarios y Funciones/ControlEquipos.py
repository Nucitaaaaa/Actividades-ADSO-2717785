
#Creación de variables, diccionarios, listas y funciones

laps = {} #Diccionario para almacenar la info de los equipos


def agregar(desktopId, perifericos, hall):
    # Revisa si el equipo ya existe en la lista
    if desktopId not in laps:
        # De lo contrario, si no existe, agrega el equipo con su ambiente y periféricos
        laps[desktopId] = {
            'ambiente': hall,
            'perifericos': perifericos,
            'novedades': []
        }
        print(f"\nEl equipo \"{desktopId}\" fue agregado exitosamente\n")
    else:
        print(f"\nEl equipo \"{desktopId}\" ya existe\n")

def novedad(desktopId, date, descripcion):
    # Revisa si el equipo con el ID dado si esta en la lista
    if desktopId in laps:
        # Si existe agrega una nueva novedad con la fecha y su descripción
        laps[desktopId]['novedades'].append({'fecha': date, 'descripcion': descripcion})
        print(f"\nLa novedad sobre el equipo {desktopId} fue agregada exitosamente\n")
        # De lo contrario muestra un mensaje de que no existe ningun equipo con esa ID
    else:
        print(f"\nNo se encontró un equipo con el ID {desktopId}")

def buscar(desktopId):
    # Revisa si el equipo con el ID dado si esta en la lista
    if desktopId in laps:
        # Si existe este va a recopilar toda la info existente sobre este equipo
        lap = laps[desktopId]
        infoDis = f"Perifericos: {lap['perifericos']}\nAmbiente: {lap['ambiente']}"
        infoNov = "\n".join([f"Fecha: {novedad['fecha']} \ Descripción: {novedad['descripcion']}" for novedad in lap['novedades']])
        print(f"\nInformación sobre el equipo {desktopId}:\n{infoDis}\n\nNovedades:\n{infoNov}\n")
        # De lo contrario muestra un mensaje de que no existe ningun equipo con esa ID 
    else:
        print(f"\nNo se encontró un equipo con el ID {desktopId}")

def reportes(opcR):
    if opcR == 1:
        # Función para generar un reporte de todas las novedades de los equipos de X ambiente
        def reportePorAmbiente(ambiente):
            for desktopId, lap in laps.items():  
                if ambiente == lap['ambiente']: #valida si el equipo pertenece a el ambiente 
                    infoNov = "\n".join([f"Fecha: {novedad['fecha']} \ Descripción: {novedad['descripcion']}\n" for novedad in lap['novedades']])
                    print(f"\nNovedades del equipo {desktopId} del ambiente {ambiente}:\n\nEquipo {desktopId}\nNovedades:\n{infoNov}")
                else: #si no pertenece, continua con el siguiente elemento de el diccionario 
                    continue

        reportePorAmbiente(str(input('Ingrese el nombre del ambiente: '))) #Llamado a la función

    elif opcR == 2:
        # Función para generar un reporte de todas las novedades de los equipos que hayan en nuestro sistema
        def reporteTotal():
            if laps:
                # Muestra las novedades de todos los equipos registrados
                for desktopId, lap in laps.items():
                    infoNov = "\n".join([f"Fecha: {novedad['fecha']} \ Descripción: {novedad['descripcion']}\n" for novedad in lap['novedades']])
                    print(f"\nNovedades de los equipos:\n\nEquipo {desktopId}\nNovedades:\n{infoNov}")
            else:
                # De lo contrario informara que no hay ningun equipo en nuestro sistema
                print("\nNo hay equipos registrados todavia.\n")
        
        # Hace el reporte total de los equipos existentes
        reporteTotal() #Llamado a la función

    else:
        # Mensaje para informar que la opción que eligio el usuario no es una valida
        print('\nOpción no valida, Seleccione (1 o 2)')

def eliminar(desktopId):
    #Funcion para eliminar un equipo del diccionario
    if desktopId in laps: #en caso de que se encuentre
        laps.pop(desktopId)   
        print(f'\nEl equipo {desktopId} ha sido eliminado del sistema')
    else: #si no se encuentra el equipo
        print(f"\nNo se encontró un equipo con el ID {desktopId}")

def modificar(desktopId, perifericos, hall):
    #funcion para modificar un equipo del diccionario 
        if desktopId in laps: #si se encuentra, se reemplazan la info anterior con la info de los argumentod
            laps[desktopId] = {
                'ambiente': hall,
                'perifericos': perifericos,
            }
            print(f"\nEl equipo {desktopId} fue modificado exitosamente\n")
        else: #si no se encuentra el equipo
            print(f"\nEl equipo {desktopId} no existe\n")
#Ejecución del programa

while True: 
    # Menu Inicial
    print('\nBienvenido al sistema de control de equipos de la nave 4 del SENA, seleccione:\n- 1 para agregar un equipo\n- 2 para agregar una novedad\n- 3 para buscar un equipo\n- 4 para mostrar el reporte\n- 5 para eliminar un equipo\n- 6 para modificar un equipo\n- 0 para salir\n\nRecuerde que para que funcionen las opciones 2, 3, 4, 5 y 6 debe agregar un equipo previamente')

    opc = int(input('\nDigite la opción: '))

    if opc == 0:
        print('\nGracias por usar este programa :D')
        break # Cierre del programa
    elif opc == 1:
        # Llamado a la funcion para Agregar un equipo
        agregar(str(input('\nIngrese el ID del equipo: ')),int(input('Ingrese la cantidad de perifericos (Ej: 2): ')),str(input('Ingrese el nombre del ambiente (Ej: D): ')))
    elif opc == 2:
        # Llamado a la funcion para Agregar una novedad
        novedad(str(input('\nIngrese el ID del equipo: ')),str(input('Ingrese la fecha en la que ocurrió la novedad (Ej: 12/10/2023): ')),str(input('Describa la novedad aquí: ')))
    elif opc == 3:
        # Llamado a la funcion para Buscar un equipo
        buscar(str(input('\nIngrese el ID del dispositivo a buscar: ')))
    elif opc == 4:
        # Llamado a la funcion para Mostrar el reporte solicitado
        reportes(int(input('\nIngrese 1 para ver el reporte de los equipos por ambiente, ingrese 2 para ver el reporte de todos los equipos: ')))
    elif opc == 5:
        eliminar(str(input('\nIngrese el id del equipo a eliminar: ')))
    elif opc == 6:
        modificar(str(input('\nIngrese el ID del equipo: ')),int(input('Ingrese la cantidad de perifericos (Ej: 2): ')),str(input('Ingrese el nombre del ambiente (Ej: D): ')))
    else:
        # Mensaje si la opción seleccionada no es valida
        print('\nDigite una opcion valida (1, 2, 3, 4, 5, 6 y 0)')