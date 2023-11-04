
#Creación de variables, diccionarios, listas y funciones

laps = {} #Diccionario para almacenar la info de los equipos

def agregar(desktopId, perifericos, hall):
    if desktopId not in laps:
        laps[desktopId] = {
            'ambiente': hall,
            'perifericos': perifericos,
            'novedades': []
        }
        print(f"\nEl equipo \"{desktopId}\" fue agregado exitosamente.\n")
    else:
        print(f"\nEl equipo \"{desktopId}\" ya existe\n")

def novedad(desktopId, date, descripcion):
    if desktopId in laps:
        laps[desktopId]['novedades'].append({'fecha': date, 'descripcion': descripcion})
        print(f"\nLa novedad sobre el equipo \"{desktopId}\" fue agregada exitosamente\n")
    else:
        print(f"\nNo se encontró un equipo con el ID {desktopId}.")

def buscar(desktopId):
    if desktopId in laps:
        lap = laps[desktopId]
        infoDis = f"Perifericos: {lap['perifericos']}\nAmbiente: {lap['ambiente']}"
        infoNov = "\n".join([f"Fecha: {novedad['fecha']} \ Descripción: {novedad['descripcion']}" for novedad in lap['novedades']])
        print(f"\nInformación sobre el equipo {desktopId}:\n{infoDis}\n\nNovedades:\n{infoNov}\n")
    else:
        print(f"\nNo se encontró un equipo con el ID {desktopId}.")

def reportes(opcR):
    if opcR == 1:
        def reporteIndividual(desktopId):
            if desktopId in laps:
                infoNov = "\n".join([f"Fecha: {novedad['fecha']} \ Descripción: {novedad['descripcion']}\n" for novedad in laps[desktopId]['novedades']])
                print(f"\nNovedades del equipo {desktopId}:\n\nEquipo {desktopId}\nNovedades:\n{infoNov}")
            else:
                print("\nNo se encuentra el equipo.\n")

        reporteIndividual(str(input('Ingrese el ID del equipo: ')))

    elif opcR == 2:
        def reporteTotal():
            if laps:
                for desktopId, lap in laps.items():
                    infoNov = "\n".join([f"Fecha: {novedad['fecha']} \ Descripción: {novedad['descripcion']}\n" for novedad in lap['novedades']])
                    print(f"\nNovedades de los equipos:\n\nEquipo {desktopId}\nNovedades:\n{infoNov}")
            else:
                print("\nNo hay equipos registrados todavia.\n")
        
        reporteTotal()

    else:
        print('\nOpción no valida')
        

#Ejecución del programa

while True: 
    print('\nBienvenido al sistema de control de quipos de la nave 4 del SENA, seleccione:\n- 1 para agregar un equipo\n- 2 para agregar una novedad\n- 3 para buscar un equipo\n- 4 para mostrar el reporte\n- 0 para salir\n\nRecuerde que para que funcionen las opciones 2, 3 y 4 debe agregar un equipo previamente.')

    opc = int(input('\nDigite la opción: '))

    if opc == 0:
        print('\nGracias por usar este programa :D')
        break
    elif opc == 1:
        agregar(str(input('\nIngrese el ID del equipo: ')),int(input('Ingrese la cantidad de perifericos (Ej: 2): ')),str(input('Ingrese el nombre del ambiente (Ej: D): ')))
    elif opc == 2:
        novedad(str(input('\nIngrese el ID del equipo: ')),str(input('Ingrese la fecha en la que ocurrió la novedad (Ej: 12/10/2023): ')),str(input('Describa la novedad aquí: ')))
    elif opc == 3:
        buscar(str(input('\nIngrese el ID del dispositivo a buscar: ')))
    elif opc == 4:
        reportes(int(input('\nIngrese 1 para ver el reporte de un equipo en especifico, ingrese 2 para ver el reporte de todos los equipos: ')))
    else:
        print('\nDigite una opcion valida')



