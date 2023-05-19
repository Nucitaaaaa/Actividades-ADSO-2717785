"""
Diseñe un algoritmo que capture dos números, y que realice la suma de
dichos números, y mostrar los datos si el resultado no es negativo.
"""

num1 = int(input("Ingrese el primer numero"))
num2 = int(input("Ingrese el segundo numero"))

sum = num1 + num2

if sum > 0:  
    print(f"El resultado de la suma es: {sum}")
else:
    print("La suma debe dar como resultado un numero positivo")