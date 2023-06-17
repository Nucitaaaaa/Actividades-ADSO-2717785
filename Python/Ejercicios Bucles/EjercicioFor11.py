
#*Elabore un algoritmo que pregunte cuántas temperaturas se van a introducir, pida esas temperaturas, y escriba la temperatura más alta, la más baja y la temperatura promedio.

#*Forma 1

numTemp = int(input("Ingrese el numero de temperaturas quiere ingresar: "))
temps = []
prom = 0

for i in range(1, numTemp + 1):
    print(f"Ingrese la {i} temperatura:", end=" ")
    temp = float(input())
    temps.append(temp)
    prom += temp
    
mayor = max(temps)
menor = min(temps)
prome = prom / len(temps)

print(f"La temperatura mayor es: {mayor}")
print(f"La temperatura menor es: {menor}")
print(f"La temperatura promedio es {prome}")



#*Forma 2

numTemp = int(input("Ingrese el numero de temperaturas quiere ingresar: "))
count = 0
acum = 0

for i in range(numTemp):
    print(f"Ingrese la {i} temperatura:", end=" ")
    temp = float(input())

    if count == 0:
        maxi = temp 
        mini = temp
    else:
        if temp > maxi:
            maxi = temp
        elif temp < mini:
            mini = temp
    
    acum += temp
    count += 1

prome = acum / numTemp

print(f"La temperatura mayor es: {maxi}")
print(f"La temperatura menor es: {mini}")
print(f"La temperatura promedio es {prome}")




