
"""
La tienda sofia valida el valor de la compra si el valor de la compra es mayor
a 40 mil , si es así debe indicar el color de la balota(roja 10%, blanca 15%,
negra 20%,amarilla 20%, verde 30%) según el color se aplica el descuento, se
debe mostrar el descuento y el valor neto a pagar.
Si los valores son menores que 40 no va aplicar ningún descuento.
"""

price = int(input("Enter the value of the purchase: "))
number = int(input("Enter how many smock you are going to buy: "))

if price > 40000:
    smock = str(input("Enter the color of the smoke: "))
    if smock.upper() == "RED":
        discount = price * .10
        discountNum = discount * number
        price = (price * number) - discountNum
        print(f"The price will be ${price} with a discount of ${discountNum}")
    elif smock.upper() == "WHITE":
        discount = price * .15
        discountNum = discount * number
        price = (price * number) - discountNum
        print(f"The price will be ${price} with a discount of ${discountNum}")
    elif smock.upper() == "BLACK":
        discount = price * .20
        discountNum = discount * number
        price = (price * number) - discountNum
        print(f"The price will be ${price} with a discount of ${discountNum}")
    elif smock.upper() == "YELLOW":
        discount = price * .20
        discountNum = discount * number
        price = (price * number) - discountNum
        print(f"The price will be ${price} with a discount of ${discountNum}")
    elif smock.upper() == "GREEN":
        discount = price * .30
        discountNum = discount * number
        price = (price * number) - discountNum
        print(f"The price will be ${price} with a discount of ${discountNum}")
    else:
        print("Enter a valid color...")
else:
    print(f"The price will be ${price} without any discount")