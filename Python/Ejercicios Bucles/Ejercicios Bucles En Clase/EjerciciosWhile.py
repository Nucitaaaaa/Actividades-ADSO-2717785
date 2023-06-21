
#1
"""
count = 0

while count < 4:
    print(count)
    count += 1
"""

#2
"""
res = input("Digite 1 o 5 para continuar: ")

while not(res.strip() == "1" or res.strip() == "5"):
    res = int(input("Digite 1 o 5 para continuar: "))

print("Obediente :D")
"""

#3
"""
name = str(input("Digite un nombre: "))
names = []
count = 1

while True:
    names.append(name)
    name = print(f"Digite el {count + 1} nombre, si quiere terminar de introducir, digite Salir: ", end=" ")
    name = input()

    count += 1

    if (name.strip().upper() == "SALIR"):
        break

print(f"Usted ha introducido {count - 1} nombres! estos son: \n {names}")
"""

#4
"""
count = 0

while count <= 10:
    print(count)
    count += 1

    if count == 8:
        break
"""

#5
"""
num = 1

while True:
    num += 1
    if num % 5 == 0:
        continue
    if num == 16:
        break
    print(num)
"""

#6
#Validar que el numero es positivo, pedir que digite un numero, sumar estos numeros (acum), mostrar la suma, contar los pares y los impares

num = int(input("Digite un numero: "))

while num < 0:
    print("Ingrese un numero positivo nuevamente: ", end=" ")
    num = int(input())

#Variables
suma = 0
countEven = 0
countOdd = 0
i = 1

while i <= num:
    suma += i
    if i % 2 == 0:
        countEven += 1
    else:
        countOdd += 1
    i += 1

print(f"La suma total es: {suma}\n Hay {countEven} pares y {countOdd} impares")
