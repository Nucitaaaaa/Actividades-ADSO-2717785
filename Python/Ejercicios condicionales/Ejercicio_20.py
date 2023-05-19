
"""
Algoritmo para hallar el área de un cuadrado si el valor del lado es mayor a
10, de lo contrario generar un mensaje de “no aplica”.
"""

side1 = float(input("Enter the first side: "))
side2 = float(input("Enter the second side: "))

area = side1 * side2

if side1 and side2 > 10 and side1 == side2 and side2 == side1:
    print(f"The area is {area}")
else:
    print("Not apply...")