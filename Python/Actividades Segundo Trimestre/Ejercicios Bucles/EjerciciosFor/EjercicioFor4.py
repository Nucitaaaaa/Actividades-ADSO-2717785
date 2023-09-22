
#*Sumar pares desde 0 hasta el numero que indique el usuario 

num = int(input("Digite un numero aquí: "))
acum = 0

for i in range(0, num + 1, 2):
    acum += i

print(f"El resultado de la suma de los numeros pares de {num} es {acum}")
