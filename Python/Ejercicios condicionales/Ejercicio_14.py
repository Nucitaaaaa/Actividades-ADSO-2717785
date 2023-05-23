
"""
Un trabajador necesita calcular su salario semanal, el cual se obtiene de la
siguiente manera: si trabaja 20 horas o menos se le paga $10.000 por hora; si
trabaja más de 20 horas se le paga $35.000 por hora.
"""

hours = float(input("Enter the hours you have worked this week: "))

if hours < 20:
    print("the hourly rate of pay will be $10000")
    pay = hours * 10000
    print(f"Your salary will be {pay}")
else:
    print("the hourly rate of pay will be $35000")
    pay = hours * 35000
    print(f"Your salary will be {pay}")

