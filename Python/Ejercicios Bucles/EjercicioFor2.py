
#*Digite un número, si el numero supera a 10, multiplique los 10 primeros números, si no, súmelos.


num = int(input("Digite un numero aquí: "))

#!No entendi bien que se debia hacer en la primera condicion
if num > 10:
    acum = 1
    for i in range(1, 11):
        acum *= i
    print(f"El resultado de la multiplicación de los primeros 10 numeros de {num} es: {acum}")
else:
    acum = 0
    for i in range(0, num):
        op = i + num
        acum += op
    print(f"El resultado es: {acum}")       