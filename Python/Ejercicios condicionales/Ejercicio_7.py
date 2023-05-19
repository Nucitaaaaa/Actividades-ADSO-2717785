
"""
Diseñe un algoritmo que lea el nombre del estudiante, el valor de su
matrícula en un curso que responda si¿ Es egresado de la universidad?, si la
respuesta es SI, se le aplica un 30 % descuento. Muestre el nombre del
estudiante y el valor de la matricula a pagar
"""

name = str(input("Enter your name: "))
tuitonFee= float(input("enter the value of the tuition: "))
graduate = str(input("Are you graduate?: "))

discount = tuitonFee - (tuitonFee * 0.3)

if graduate == "yes" or graduate == "YES" or graduate == "Yes":
    tuitonFee = discount
    print(f"")
