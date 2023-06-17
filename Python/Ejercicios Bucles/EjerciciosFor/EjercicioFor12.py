
# #*Elaborar un algoritmo que pida las 4 notas de n estudiantes e imprima la nota más alta, la más baja y el promedio.

# #*Forma1

# totalNotas = []
# acum = 0

# for i in range(1,4+1):
#     print(f"Ingrese la {i} nota:", end=" ")
#     nota = float(input())
#     totalNotas.append(nota)
#     acum += nota

# mayor = max(totalNotas)
# menor = min(totalNotas)
# prom = acum / len(totalNotas)

# print(f"La nota mayor es {mayor}")
# print(f"La nota menor es {menor}")
# print(f"El promedio de las notas es {prom}")


#*Forma2

acum = 0
count = 0

for i in range(1,4+1):
    print(f"Ingrese la {i} nota:", end=" ")
    nota = float(input())
    acum += nota

    if count == 0:
        mayor = nota
        menor = nota
    else:
        if nota > mayor:
            mayor = nota
        elif nota < menor:
            menor = nota

    count += 1
    prom = acum / count

print(f"La nota mayor es {mayor}")
print(f"La nota menor es {menor}")
print(f"El promedio de las notas es {prom}")

