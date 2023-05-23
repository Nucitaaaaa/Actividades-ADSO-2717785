
"""
En un Almacén de cadena, se hace una promoción mediante la cual el
cliente obtiene un descuento dependiendo de un número que se escoge al
azar, si el número escogido es menor a 65 el descuento es del 20% sobre el
total de la compra si es mayor o igual a 65 el descuento es del 30%
"""

number = int(input("Enter a number, ¡and we will make you a special discount!: "))
price = int(input("Enter the price of the product: "))

if number < 65:
    print("The discount will be of 20%")
    discount = price * .20
    price -= discount
    print(f"The price will be ${price} with a discount of ${discount}")
else:
    print("The discount will be of 30%")
    discount = price * .30
    price -= discount
    print(f"The price will be ${price} with a discount of ${discount}")