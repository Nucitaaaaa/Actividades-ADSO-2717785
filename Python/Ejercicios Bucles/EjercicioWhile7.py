
#*Leer números enteros del teclado, hasta que el usuario ingrese el 0. Finalmente, mostrar la sumatoria de todos los números ingresados.

end = 0
suma = 0

while not end:
    n = int(input("Ingrese todos los numeros enteros del teclado: "))
    suma += n
    if n == end:
        print(f"La suma de los numeros del teclado ingresados es {suma}")
        break
