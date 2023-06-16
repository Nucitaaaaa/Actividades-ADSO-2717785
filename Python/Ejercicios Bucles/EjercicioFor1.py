
#*Suma de los n primeros números, solicite al usuario el numero de elementos a sumar

#!No se si era así, lo que entendi es que se debian los numeros desde 0 hasta el numero que digite el usuario y luego mostrar el resultado.

suma = int(input("Digite la cantidad de numeros que quiere sumar: "))
acum = 0

for i in range(0, suma):
    print(f"Numero: {i}")
    op = i + suma
    print(f"Operacion: {op}")
    acum += op
    print(f"Suma: {acum}")

print(acum)