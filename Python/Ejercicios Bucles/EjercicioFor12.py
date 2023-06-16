
#*Elaborar un algoritmo que pida las 4 notas de n estudiantes e imprima la nota más alta, la más baja y el promedio.

totalNotas = []
acum = 0

for i in range(1,4+1):
    print(f"Ingrese la {i} nota:", end=" ")
    nota = float(input())
    totalNotas.append(nota)
    acum += nota

mayor = max(totalNotas)
menor = min(totalNotas)
prom = acum / len(totalNotas)

print(f"La nota mayor es {mayor}")
print(f"La nota menor es {menor}")
print(f"El promedio de las notas es {prom}")
