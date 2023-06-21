
#1
"""
#Forma 1
for i in range(1,11):
    if i % 2 == 0:
        print(i)

#Forma2
for i in range(0,11,2):
        print(i)

#Forma3
count = 0
for i in range(1,11):
    if i % 2 == 0:
        count += i
print(f"Los numeros pares que hay son {i}")

"""

#2

acum = 0
countPar = 0
countImpar = 0

for i in range(1,11):
    acum += i
    if i % 2 != 0:
        countPar += 1
    else:
        countImpar += 1

print(f"La suma de todos los numeros es {acum}\nlos numeros pares son {countPar}\nlos impares son {countImpar}")


