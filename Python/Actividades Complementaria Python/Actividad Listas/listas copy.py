
#1
#Aprendices insertados manualmente para que el codigo funcione
aprendices = ["Sebastian Tovar","Juan Mahecha","Maria Buenaventura","Mathew Guarnizo","Kevin Hernan","Melissa Lopez","Vanesa Ladino","Stiven Ramirez","Esteban Prada","Kevin Botero","Sebastian Pinzon","Camila Alape","Kevin Londoño","Nicolas Fierro","Santiago Gomez","Marlon Lopez","Stiwar Perez","Miguel Bernal","Maria Molano","Nicolas Paulo","Laura Benavides","Wilfrank Bermudez","Dahiana Rivera","Paula Garcia","Maria Jose Perez","Nataly Montaña","Lina Barrios","Cristian Peña","Yency Quiñonez"]

#Edades de los aprendices insertados manualmente para que el codigo funcione
edadesAprendices = [17,17,17,17,17,16,17,18,17,17,17,18,23,18,17,19,18,17,18,17,17,18,18,19,17,17,18,17,17]


#*Codigo para insertar los aprendices manualmente
# Aprendices = []
# EdadesAprendices = []
# count = 0

# while count < 30:
#     aprendiz = str(input("Ingrese el nombre del aprendiz: "))
#     aprendices.append(aprendiz)

#     edad = int(input("Ingrese la edad del aprendiz: "))
#     edadesAprendices.append(edad)

#     count += 1


#2. Mostrar los aprendices y las edades de los aprendices 
print(f"\nAprendices: {aprendices}\n")
print(f"Edades de los aprendices: {edadesAprendices}\n")


#3. Muestre el nombre del aprendiz con mayor edad
#Se selecciona el aprendiz con mayor edad
edadMayor = max(edadesAprendices)
#Se selecciona el indice de ese aprendiz
iAprendizMayor = aprendices.index(edadMayor) #;D
#Se selecciona el nombre en base al indice de la edad
aprendizMayor = aprendices[iAprendizMayor]

#Se muestra el aprendiz
print(f"El aprendiz con mayor edad es {aprendizMayor} con {edadMayor} años\n")


#4. Muestre el nombre de la instructora en posición 1 (0)
aprendices.insert(0,"Adriana Rincon")
edadesAprendices.insert(0,35) #!edad inventada :3

print(f"Aprendices: {aprendices}\n")
print(f"Edades de los aprendices: {edadesAprendices}\n")


#5.Cuente cuantos aprendices tienen 18 años
aprendicesCon18 = edadesAprendices.count(18)

print(f"{aprendicesCon18} aprendices tienen 18 años\n")


#6. Agregue a un aprendiz al final de la lista
aprendices.append("Matias Guzman")
edadesAprendices.append(17)

print(f"Aprendices: {aprendices}\n")
print(f"Edades de los aprendices: {edadesAprendices}\n")


#7. Borre el nombre de la instructora de la lista
aprendices.remove(aprendices[1]) #;D
edadesAprendices.remove(edadesAprendices[1])

print(f"Aprendices: {aprendices}\n")
print(f"Edades de los aprendices: {edadesAprendices}\n")


#8. Indique un dato a buscar en la lista de aprendices
nombreAprendiz = str(input("Indique el nombre del aprendiz a buscar: ")) #se crea un input para escribir el nombre del aprendiz
coincidencias = 0 #se crea un contador 

for aprendiz in aprendices: #se hace un bucle donde se valida si el nombre del aprendiz se encuentra en la lista
    if nombreAprendiz == aprendiz:
        print(f"\nEl estudiante {nombreAprendiz} si se encuentra en la lista de estudiantes\n") #si si se encuentra
        coincidencias = 1

#;D 

if coincidencias == 0: #si el contador no subió
    print(f"\nEl estudiante {nombreAprendiz} no se encuentra en la lista de estudiantes\n")
    


#9. Muestre los primeros 10 aprendices de la lista
print(f"Los 10 primeros aprendices de la lista son: {aprendices[0:10]}\n") #se selecciona el indice del 0 al 10
print(f"Las edades de 10 primeros aprendices son: {edadesAprendices[0:10]}\n")


#10. Muestre los ultimos 10 aprendices de la lista
print(f"Los 10 ultimos aprendices de la lista son: {aprendices[20:30]}\n") #se selecciona el indice del 20 al 30
print(f"Las edades de los 10 ultimos apredices son: {edadesAprendices[20:30]}\n")


#11
print(f"Los aprendices del 10 al 20 en la lista son: {aprendices[10:20]}\n") #se selecciona el indice del 10 al 21
print(f"Las edades de los aprendices del 10 al 20 son: {edadesAprendices[10:20]}\n")
