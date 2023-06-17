
#*Hacer un programa que pida dos números y muestre todos los números que van desde el primero al segundo, validar que el primer número sea menor que el segundo.

num1 = int(input("Digite un numero: "))
num2 = int(input("Digite otro numero MAYOR al numero anterior: "))

if num1 < num2:
    print(f"Los numeros que van desde {num1} hasta {num2} son:")
    for i in range(num1, num2 + 1):
        print(i)
else:
    print("El segundo numero debe ser MAYOR al primero")
