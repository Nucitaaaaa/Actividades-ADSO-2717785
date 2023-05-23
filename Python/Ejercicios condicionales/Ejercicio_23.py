
"""
Un cliente va a comprar una moto y se percata que si lo compraba el día
martes tiene un descuento del 10%, luego si lo compra el día sábado tiene
un descuento del 18% mostrar cuanto pagara en cada opción.
"""

day = str(input("Enter the day you will purchase your motorcycle: "))
price = int(input("Enter the price of your motorcycle: "))

if day == "TUESDAY" or day == "Tuesday" or day == "tuesday":
    discount = price * .10
    price -= discount
    print(f"The price will be ${price} with a discount of ${discount}")
elif day == "SATURDAY" or day == "Saturday" or day == "saturday":
    discount = price * .18
    price -= discount
    print(f"The price will be ${price} with a discount of ${discount}")
else:
    print(f"The price will be ${price} without any discount")