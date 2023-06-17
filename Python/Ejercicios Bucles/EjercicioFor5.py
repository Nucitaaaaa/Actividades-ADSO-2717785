
#*Hacer un programa que imprima la suma de todos los números impares desde 1 hasta n, y diga cuantos números impares hay

def odd():
    n = int(input("Digite un numero: "))
    acum = 0
    suma = 0

    for i in range(0, n + 1):
        if i % 2 != 0:
            suma = i + acum
            acum += 1
    
    print(f"La suma de todos los numeros impares que hay desde 0 hasta {n} es: {suma}")
    print(f"Los numeros impares que hay desde 0 hasta {n} son: {acum}")

odd()