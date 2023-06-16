
#*Algoritmo que pregunte al usuario que tabla de multiplicar quiere ver, debe generar la tabla de multiplicar desde cero hasta 10.

multi = int(input("Ingrese el numero la tabla de multiplicar que desee ver: "))

for i in range(1,11):
    print(f"{multi} * {i} es igual a {multi * i}")