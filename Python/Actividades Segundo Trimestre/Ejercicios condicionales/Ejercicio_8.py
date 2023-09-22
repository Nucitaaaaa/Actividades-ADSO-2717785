
"""
Diseñar un algoritmo que muestre si una persona tiene ingresos o no, debe
indicarlos ingresos y egresos, se debe validar el saldo , pero para ser más específicos se responderá a las siguientes preguntas:

- Si no tiene efectivo entonces está en números rojos.
- Si tiene poco efectivo menor a 2000, que muestre que debe esforzarse por
trabajar más.
- Si tiene un efectivo menor a 3000 entonces significa que le va regularmente
bien.
- Si tiene un efectivo mayor a 3000 entonces significa que tiene buen status
financiero
"""

income = float(input("Enter your income: "))
expenses = float(input("Enter your expenses: "))

cash = income - expenses

if cash <= 0:
    print("¡You are bankrupt!")
elif cash > 0 and cash < 2000:
    print("You must work a little more...")
elif cash >= 2000 and cash < 3000:
    print("¡You're doing well!")
elif cash >= 3000:
    print("¡Keep it up!, you're doing great, you have a good financial status. ")
