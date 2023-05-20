
"""
Realice un menú donde el usuario deberá seleccionar una opción de las
operaciones básicas, y se le solicite al usuario digitar dos números, y
dependiendo de la respuesta realice cada operación
"""

menu = 0

while menu == 0:

    print("\nbasic calculator")
    print("Enter:\n\n1 for addition\n2 for subtraction\n3 for multiplication\n4 for division\n9 to exit the calculator")

    operation = int(input("\nEnter the number of the operation to be carried out: "))

    if operation == 9:
        print("\nThank you for using this calculator")
        break
    
    else: 
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        
        if operation == 1:
            summ = num1 + num2
            print(f"\nThe result of the addition is: {summ}")
            print(" ")
        elif operation == 2:
            sub = num1 - num2
            print(f"\nThe result of the subtraction is: {sub}")
            print(" ")
        elif operation == 3:
            multi = num1 * num2
            print(f"\nThe result of the multiplication is: {multi}")
            print(" ")
        elif operation == 4:
            divi = num1 / num2
            print(f"\nThe result of the division is: {divi}")
            print(" ")
        else:
            print("\nEnter a valid operation number")
