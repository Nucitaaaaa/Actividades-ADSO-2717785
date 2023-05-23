
"""
Diseñe un algoritmo que lea el nombre del estudiante, el valor de su
matrícula en un curso que responda si¿ Es egresado de la universidad?, si la
respuesta es SI, se le aplica un 30 % descuento. Muestre el nombre del
<<<<<<< HEAD
estudiante y el valor de la matricula a pagar
"""

name = str(input("Enter your name: "))
tuitonFee= float(input("enter the value of the tuition: "))
graduate = str(input("Are you graduate?: "))

discount = tuitonFee - (tuitonFee * 0.3)

if graduate == "yes" or graduate == "YES" or graduate == "Yes":
    tuitonFee = discount
    print(f"")
=======
estudiante y el valor de la matricula a pagar.

"""

name = str(input("Enter your name: "))
tuitionFee = float(input("Enter the value of the tuition: "))
graduate = str(input("Are you graduate?: "))

discount = tuitionFee - (tuitionFee * 0.3)

if graduate == "yes" or graduate == "YES" or graduate == "Yes":
    tuitionFee = discount
    print(f"¡You have a discount {name}!, the value of your tuiton will be: ${tuitionFee} ")
else:
    print(f"{name}, The value of your tuiton will be: ${tuitionFee} ")
>>>>>>> 0d627d0f1410373118337e5458cd5267e1e2b45b
