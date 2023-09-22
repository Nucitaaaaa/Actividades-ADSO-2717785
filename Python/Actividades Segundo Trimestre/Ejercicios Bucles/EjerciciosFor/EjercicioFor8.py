
#*Un maestro de escuela necesita un algoritmo que capture n notas de un estudiante y calcule el promedio.

n = int(input("Digite el numero de notas al que le quiere sacar el promedio: "))
acum = 0

for i in range(1, n + 1):
    print(f"Digite la {i} nota:", end=" ")
    nota = int(input())
    acum += nota
    promedio = acum / n 

print(f"El promedio de las notas es {promedio}")

