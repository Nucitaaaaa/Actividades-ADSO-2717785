
#*Sumar pares desde 0 hasta el numero que indique el usuario

n = int(input("Digite un numero: "))
suma = 0
pares = 0
count = 0

while count <= n:
    if count % 2 == 0:
        suma += count
        pares += 1
    count += 1

print(f"Los numeros pares dentro del numero {n} son: {pares}")
print(f"La suma de los numeros pares dentro del numero {n} es: {suma}")