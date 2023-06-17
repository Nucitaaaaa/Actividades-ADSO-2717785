
#*Un maestro de escuela necesita un algoritmo que capture n notas de un estudiante y calcule el promedio

end = 0
notas = []
suma = 0

while not end:
    nota = float(input("Ingrese la nota del estudiante aquí: "))
    salir = input("Desea sacar el promedio ahora? ingrese \"si\" para sacar el promedio: ")
    notas.append(nota)
    suma += nota
    if salir.lower() == "si":
        prom = suma / len(notas)
        print(f"El promedio de las notas es de {prom}")
        break
