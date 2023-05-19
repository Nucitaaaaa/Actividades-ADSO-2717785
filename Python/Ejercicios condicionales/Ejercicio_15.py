
"""
Hacer un algoritmo que calcule el total a pagar por la compra de camisas.
Si se compran tres camisas o más se aplica un descuento del 15% sobre el
total de la compra y si son menos de 3 camisas el descuento es del 5%.

"""

shirts = int(input("Enter the number of shirts that you will buy here: "))

if shirts > 3:
    print("The discount on T-shirts will be of 15% ")
else:
    print("The discount on T-shirts will be of 5% ")