
"""
La empresa Auteco de motocicletas tiene una promoción de mitad de año,
que consiste en lo siguiente. Las motos marca Honda tienen un descuento
del 4%, las marcas Yamaha del 7% y las Suzuki del 15%, las otras marcas 3%.

"""

brand = str(input("Enter the motorcycle brand: "))
price = int(input("Enter the price of the motorcycle: "))

if brand == "HONDA" or brand == "Honda" or brand == "honda":
    print("This brand of motorcycle offers a discount of 4%")
    discount = price * .04
    price -= discount
    print(f"The price will be ${price} with a discount of ${discount}")

elif brand == "YAMAHA" or brand == "Yamaha" or brand == "yamaha":
    print("This brand of motorcycle offers a discount of 7%")
    discount = price * .07
    price -= discount
    print(f"The price will be ${price} with a discount of ${discount}")

elif brand == "SUZUKI" or brand == "Suzuki" or brand == "suzuki":
    print("This brand of motorcycle offers a discount of 15%")
    discount = price * .15
    price -= discount
    print(f"The price will be ${price} with a discount of ${discount}")

else:
    print("This brand of motorcycle offers a discount of 3%")
    discount = price * .03
    price -= discount
    print(f"The price will be ${price} with a discount of ${discount}")