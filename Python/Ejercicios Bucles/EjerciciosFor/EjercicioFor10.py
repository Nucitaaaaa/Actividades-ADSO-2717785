
#*Elabore un algoritmo que pida un número entero mayor que cero y que escriba sus divisores. Validar que el usuario haya ingresado un número mayor a cero.

n = int(input("Ingrese un numero MAYOR A 0: "))

if n > 0:
    for i in range(1,n + 1): 
        if n % i == 0:
            print(f"{i} es divisor de {n}")
else:
    print("El numero debe ser MAYOR a 0...")