
#*Hacer un programa que imprima la suma de todos los números impares desde 1 hasta n, y diga cuantos números impares hay.


n = int(input("Ingrese un numero: "))
count = 0
suma = 0

print(f"Los numeros impares que hay desde 1 hasta {n} son:")
while count != n+1:
    if count % 2 != 0:
        suma += count 
        print(count)
    count += 1
print(f"La suma de los numeros impares que hay desde 1 hasta {n} es: {suma}")