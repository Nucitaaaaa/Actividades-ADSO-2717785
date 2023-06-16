
#*Elabore un algoritmo que pregunte cuántas temperaturas se van a introducir, pida esas temperaturas, y escriba la temperatura más alta, la más baja y la temperatura promedio.

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




    


