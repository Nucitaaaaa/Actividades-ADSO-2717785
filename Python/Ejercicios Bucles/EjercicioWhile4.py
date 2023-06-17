
#*Hacer un programa que pida dos números y muestre todos los números que van desde el primero al segundo, validar que el primer número sea menor que el segundo

n1 = int(input("Ingrese el primer numero: "))
n2 = int(input("Ingrese el segundo numero: "))
count = n1
num = 0

if n1 < n2:
    print(f"Los numeros que estan entre {n1} y {n2} son:")
    while count != n2 - 1:
        num += count
        count += 1
        print(count)
else:
    print("El primer numero debe ser menor al segundo")
