
"""
Realice un menú donde el usuario deberá seleccionar una opción de las
operaciones básicas, y se le solicite al usuario digitar dos números, y
dependiendo de la respuesta realice cada operación
"""
print("Calculadora Basica\n")
print("Digite:\n\n1 Para suma\n2 Para resta\n3 Para multiplicación\n4 Para división")

operacion = int(input("\nDigite el numero de la operación a realizar: "))

num1 = int(input("Digite el primer numero: "))
num2 = int(input("Digite el segundo numero: "))

if operacion == 1:
    suma = num1 + num2
    print("\nEl resultado de la suma es:", suma)
    print(" ")
elif operacion == 2:
    resta = num1 - num2
    print("\nEl resultado de la resta es:", resta)
    print(" ")
elif operacion == 3:
    multi = num1 * num2
    print("\nEl resultado de la multiplicación es:", multi)
    print(" ")
elif operacion == 4:
    divi = num1 / num2
    print("\nEl resultado de la división es:", divi)
    print(" ")
else:
    print("Digite un numero de operación valido")
