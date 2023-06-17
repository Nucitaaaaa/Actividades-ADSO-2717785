
#*Elabore un algoritmo que permita ingresar n número de temperaturas y escriba la temperatura más alta, la más baja y la temperatura promedio

temps = []
prom = 0
end = 0

while not end:
    nTemp = float(input("Ingrese aqui la temperatura: "))
    temps.append(nTemp)
    prom += nTemp
    
    if nTemp == end:
        temps.pop()

        mayor = max(temps)
        menor = min(temps)
        prom /= len(temps)

        print(f"La nota mayor es {mayor}")
        print(f"La nota menor es {menor}")
        print(f"El promedio de las notas es {prom}")
        break

