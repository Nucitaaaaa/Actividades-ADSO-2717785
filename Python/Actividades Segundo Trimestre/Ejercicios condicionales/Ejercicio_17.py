
"""
Hacer un programa que pida dos números y los imprima en forma
ascendente y descendente.
"""

num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

if num1 < num2:
    print(f"the ascending form will be {num1} , {num2}")
    print(f"the descending form will be {num2} , {num1}")
else:
    print(f"the ascending form will be {num2} , {num1}")
    print(f"the descending form will be {num1} , {num2}")