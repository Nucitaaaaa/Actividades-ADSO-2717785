laps = {}

class Desktop:
    def __init__(self, desktopId, ambiente, perifericos, novedades):
        self.desktopId = desktopId
        self.ambiente = ambiente
        self.perifericos = perifericos
        self.novedades = []

    def validarPc(desktopId):
        if desktopId not in laps:
            def agregar(id, perifericos, ambiente):
                laps[id] = {
                    'ambiente': ambiente,
                    'perifericos': perifericos,
                    'novedades': []
                }
                print(f"\nEl equipo \"{desktopId}\" fue agregado exitosamente\n")

            agregar(id = desktopId,ambiente = str(input('Ingrese el nombre del ambiente (Ej: D): ')),perifericos = int(input('Ingrese la cantidad de perifericos (Ej: 2): ')))

        else:
            print(f"\nEl equipo \"{desktopId}\" ya existe\n")

    def validarNovedad(desktopId):
        if desktopId in laps:
            def novedad(id, date, descripcion):
                
                laps[id]['novedades'].append({'fecha': date, 'descripcion': descripcion})
                print(f"\nLa novedad sobre el equipo \"{desktopId}\" fue agregada exitosamente\n")

            novedad(id = desktopId,date = str(input('Ingrese la fecha en la que ocurrió la novedad (Ej: 12/10/2023): ')),descripcion = str(input('Describa la novedad aquí: ')))
        else:
            print(f"\nNo se encontró un equipo con el ID {desktopId}")

    def buscar(desktopId):
        if desktopId in laps:
            lap = laps[desktopId]
            infoDis = f"Perifericos: {lap['perifericos']}\nAmbiente: {lap['ambiente']}"
            infoNov = "\n".join([f"Fecha: {novedad['fecha']} \ Descripción: {novedad['descripcion']}" for novedad in lap['novedades']])
            print(f"\nInformación sobre el equipo {desktopId}:\n{infoDis}\n\nNovedades:\n{infoNov}\n") 
        else:
            print(f"\nNo se encontró un equipo con el ID {desktopId}")

    def reportes(opcR):
        if opcR == 1:
            def reportePorAmbiente(ambiente):
                for desktopId, lap in laps.items():  
                    if ambiente == lap['ambiente']:
                        infoNov = "\n".join([f"Fecha: {novedad['fecha']} \ Descripción: {novedad['descripcion']}\n" for novedad in lap['novedades']])
                        print(f"\nNovedades del equipo {desktopId} del ambiente {ambiente}:\n\nEquipo {desktopId}\nNovedades:\n{infoNov}")
                    else:
                        continue

            reportePorAmbiente(str(input('Ingrese el nombre del ambiente: ')))

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
            print('\nOpción no valida, Seleccione (1 o 2)')

    def eliminar(desktopId):
        if desktopId in laps:
            laps.pop(desktopId)   
            print(f'\nEl equipo {desktopId} ha sido eliminado del sistema')
        else:
            print(f"\nNo se encontró un equipo con el ID {desktopId}")

    def validarMod(desktopId):
        if desktopId in laps:
            def modificar(id, perifericos, ambiente):
                laps[desktopId] = {
                    'ambiente': ambiente,
                    'perifericos': perifericos,
                    }
                print(f"\nEl equipo {desktopId} fue modificado exitosamente\n")

            modificar(id = desktopId, perifericos = int(input('Ingrese la cantidad de perifericos (Ej: 2): ')), ambiente= str(input('Ingrese el nombre del ambiente (Ej: D): ')))
        else:
            print(f"\nEl equipo {desktopId} no existe\n")
                        

while True: 
    print('\nBienvenido al sistema de control de equipos de la nave 4 del SENA, seleccione:\n- 1 para agregar un equipo\n- 2 para agregar una novedad\n- 3 para buscar un equipo\n- 4 para mostrar el reporte\n- 5 para eliminar un equipo\n- 6 para modificar un equipo\n- 0 para salir\n\nRecuerde que para que funcionen las opciones 2, 3, 4, 5 y 6 debe agregar un equipo previamente')

    opc = int(input('\nDigite la opción: '))

    if opc == 0:
        print('\nGracias por usar este programa :D')
        break 
    elif opc == 1:
        Desktop.validarPc(str(input('\nIngrese el ID del equipo: ')))
    elif opc == 2:
        Desktop.validarNovedad(str(input('\nIngrese el ID del equipo: ')))
    elif opc == 3:
        Desktop.buscar(str(input('\nIngrese el ID del dispositivo a buscar: ')))
    elif opc == 4:
        Desktop.reportes(int(input('\nIngrese 1 para ver el reporte de los equipos por ambiente, ingrese 2 para ver el reporte de todos los equipos: ')))
    elif opc == 5:
        Desktop.eliminar(str(input('\nIngrese el id del equipo a eliminar: ')))
    elif opc == 6:
        Desktop.validarMod(str(input('\nIngrese el ID del equipo: ')))
    else:
        print('\nDigite una opcion valida (1, 2, 3, 4, 5, 6 y 0)')