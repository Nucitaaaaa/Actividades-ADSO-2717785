
"""
Realizar el siguiente algoritmo:
Entrada: un numero, que se almacenará en una variable llamada numeroDia.
Proceso: Realizar las respectivas comparaciones para cada uno de los valores entre 1 y 7.
Salida: Mostrar el nombre del dia, segun el valor contenido en numeroDia.
"""

dayNum = int(input("Write a number from 1 to 7 and I will tell you what day of the week it is: "))

if dayNum == 1:
    print("The day of the week is Monday")
elif dayNum == 2:
    print("The day of the week is Tuesday")
elif dayNum == 3:
    print("The day of the week is Wednesday")
elif dayNum == 4:
    print("The day of the week is Thursday")
elif dayNum == 5:
    print("The day of the week is Friday") 
elif dayNum == 6:
    print("The day of the week is Saturday")
elif dayNum == 7:
    print("The day of the week is Sunday")
else:
    print("That number is not a day of the week")