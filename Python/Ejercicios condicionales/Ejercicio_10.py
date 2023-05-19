
"""
Mostrar la suma de dos números enteros, si el resultado supera a 10
"""

num1 = int(input("Enter your first num: "))
num2 = int(input("Enter your second num: "))

sum = num1 + num2

if sum > 10:
    print(f"the result is {sum}")
else:
    print("the result must be greater than 10")

    