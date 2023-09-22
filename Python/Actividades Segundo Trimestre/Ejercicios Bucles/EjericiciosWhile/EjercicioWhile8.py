
#*Elabore un algoritmo que pida un número entero mayor que cero y que escriba sus divisores. Validar que el usuario haya ingresado un número mayor a cero.

num = int(input("Digite un numero MAYOR a 0: "))
count = 1

while count != num+1:
    if num % count == 0:
        print(f"{count} es divisor de {num}")
    elif num == 0:
        print("El numero debe ser MAYOR que 0...")
    count += 1

