
"""
A un trabajador le descuentan de su sueldo el 4%, si su sueldo es menor o
igual a $1000000, si el sueldo está entre $1000000 y $2000000 el 7%, y por
encima de 2000000 el 8% calcular el descuento y sueldo neto que recibe el
trabajador dado su sueldo.
"""

salary = int(input("Enter your salary: "))

if salary <= 1000000:
    discount = salary * 0.04
    salary -= discount
    print(f"Your salary will be ${salary}, with a discount of {discount}")
elif salary > 1000000 and salary < 2000000:
    discount = salary * 0.07
    salary -= discount
    print(f"Your salary will be ${salary} with a discount of {discount}")
elif salary >= 2000000:
    discount = salary * 0.08
    salary -= discount
    print(f"Your salary will be ${salary} with a discount of {discount}")
else:
    print("Not apply...")