
"""
Hacer un programa que pida 3 números e indicar si el tercero es igual a la
suma del primero y el segundo.
"""

num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
num3 = int(input("Enter one last number: "))

if num3 == num1 + num2:
    print(f"The number \"{num3}\" is the sum of {num1} and {num2}")
else:
    print(f"The number \"{num3}\" is not the sum of {num1} and {num2}")