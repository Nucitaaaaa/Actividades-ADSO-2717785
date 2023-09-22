
"""
Indicar si entre dos números si ambos son pares o uno de ellos cual es par
"""

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if num1 and num2 % 2 == 0:
    print(f"{num1} and {num2} are even")
elif num1 % 2 == 0:
    print(f"{num1} is even and {num2} is odd")
else:
    print(f"{num1} is odd and {num2} is even")