
"""
La empresa Auteco de motocicletas tiene una promoción de mitad de año,
que consiste en lo siguiente. Las motos marca Honda tienen un descuento
del 4%, las marcas Yamaha del 7% y las Suzuki del 15%, las otras marcas 3%.

"""

brand = str(input("Enter the motorcycle brand: "))

if brand == "HONDA" or brand == "Honda" or brand == "honda":
    print("This brand of motorcycle offers a discount of 4%")

elif brand == "YAMAHA" or brand == "Yamaha" or brand == "yamaha":
    print("This brand of motorcycle offers a discount of 7%")

elif brand == "SUZUKI" or brand == "Suzuki" or brand == "suzuki":
    print("This brand of motorcycle offers a discount of 15%")

else:
    print("This brand of motorcycle offers a discount of 3%")