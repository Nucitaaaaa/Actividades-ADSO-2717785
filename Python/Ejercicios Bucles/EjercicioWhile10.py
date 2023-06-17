
#*Elaborar un algoritmo que pida las 3 notas de n estudiantes e imprima la nota más alta, la más baja y el promedio.

notas = []
prom = 0
acum = 0

while acum != 3:
    nota = float(input("Ingrese aqui la nota: "))
    notas.append(nota)
    prom += nota
    acum += 1
    
    if acum == 3:

        mayor = max(notas)
        menor = min(notas)
        prom /= len(notas)

        print(f"La nota mayor es {mayor}")
        print(f"La nota menor es {menor}")
        print(f"El promedio de las notas es {prom}")
        break
