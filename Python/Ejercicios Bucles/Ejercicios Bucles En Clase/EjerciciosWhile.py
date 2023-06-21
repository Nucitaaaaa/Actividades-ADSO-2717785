
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

count = 0

while count <= 10:
    print(count)
    count += 1

    if count == 8:
        break

