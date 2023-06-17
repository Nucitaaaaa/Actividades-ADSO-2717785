
#*Digite un número, si el numero supera a 10, multiplique los 10 primeros números, sino, súmelos.

n = int(input("Digite un numero: "))
cont = 0

if n > 10:
    acum = 1
    while cont != 10:
        cont += 1
        acum *= cont
    print(f"El resultado es: {acum}")

else:
    acum = 0
    while cont < n:
        cont += 1
        acum += cont
    print(f"El resultado es: {acum}")


