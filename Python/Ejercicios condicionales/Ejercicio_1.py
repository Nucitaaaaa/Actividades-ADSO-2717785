"""
Diseñe un algoritmo que capture dos números, y que realice la suma de
dichos números, y mostrar los datos si el resultado no es negativo.
"""

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

sum = num1 + num2

if sum > 0:  
    print(f"the result of the sum is : {sum}")
else:
    print("The sum must result in a positive number")