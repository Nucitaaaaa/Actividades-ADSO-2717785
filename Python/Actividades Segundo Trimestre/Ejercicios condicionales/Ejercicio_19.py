
"""
Dado tres números calcular cual es el mayor de los tres
"""

num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
num3 = int(input("Enter one last number: "))

if num1 > num2 and num3:
    print(f"{num1} is the largest number")
elif num2 > num1 and num3:
    print(f"{num2} is the largest number")
elif num3 > num1 and num2:
    print(f"{num3} is the largest number")