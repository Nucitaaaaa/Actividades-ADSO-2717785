
#1
aprendices = ["Sebastian Tovar","Juan Mahecha","Maria Buenaventura","Mathew Guarnizo","Kevin Hernan","Melissa Lopez","Vanesa Ladino","Stiven Ramirez","Esteban Prada","Kevin Botero","Sebastian Pinzon","Camila Alape","Kevin Londoño","Nicolas Fierro","Santiago Gomez","Marlon Lopez","Stiwar Perez","Miguel Bernal","Maria Molano","Nicolas Paulo","Laura Benavides","Wilfrank Bermudez","Dahiana Rivera","Paula Garcia","Maria Jose Perez","Nataly Montaña","Lina Barrios","Cristian Peña","Yency Quiñonez"]

edadesAprendices = [17,17,17,17,17,16,17,18,17,17,17,18,23,18,17,19,18,17,18,17,17,18,18,19,17,17,18,17,17]


#Codigo para insertar los aprendices manualmente
# count = 0

# while count < 30:
#     aprendiz = str(input("Ingrese el nombre del aprendiz: "))
#     aprendices.append(aprendiz)

#     edad = int(input("Ingrese la edad del aprendiz: "))
#     edadesAprendices.append(edad)

#     count += 1


#2
print(f"\nAprendices: {aprendices}\n")
print(f"Edades de los aprendices: {edadesAprendices}\n")


#3
edadMayor = max(edadesAprendices)
iAprendizMayor = edadesAprendices.index(edadMayor)
aprendizMayor = aprendices[iAprendizMayor]

print(f"El aprendiz con mayor edad es {aprendizMayor} con {edadMayor} años\n")


#4
aprendices.insert(0,"Adriana Rincon")
edadesAprendices.insert(0,35) #!edad inventada :3

print(f"Aprendices: {aprendices}\n")
print(f"Edades de los aprendices: {edadesAprendices}\n")


#5
aprendicesCon18 = edadesAprendices.count(18)

print(f"{aprendicesCon18} aprendices tienen 18 años\n")


#6
aprendices.append("Matias Guzman")
edadesAprendices.append(17)

print(f"Aprendices: {aprendices}\n")
print(f"Edades de los aprendices: {edadesAprendices}\n")


#7
aprendices.remove(aprendices[0])
edadesAprendices.remove(edadesAprendices[0])

print(f"Aprendices: {aprendices}\n")
print(f"Edades de los aprendices: {edadesAprendices}\n")


#8
nombreAprendiz = str(input("Indique el nombre del aprendiz a buscar: "))
coincidencias = 0

for aprendiz in aprendices:
    if nombreAprendiz == aprendiz:
        print(f"\nEl estudiante {nombreAprendiz} si se encuentra en la lista de estudiantes\n")
        coincidencias = 1
    else:
        continue

if coincidencias == 0:
    print(f"\nEl estudiante {nombreAprendiz} no se encuentra en la lista de estudiantes\n")
    


#9
print(f"Los 10 primeros aprendices de la lista son: {aprendices[0:10]}\n")
print(f"Las edades de 10 primeros aprendices son: {edadesAprendices[0:10]}\n")


#10
print(f"Los 10 ultimos aprendices de la lista son: {aprendices[20:30]}\n")
print(f"Las edades de los 10 ultimos apredices son: {edadesAprendices[20:30]}\n")


#11
print(f"Los aprendices del 10 al 20 en la lista son: {aprendices[10:21]}\n")
print(f"Las edades de los aprendices del 10 al 20 son: {edadesAprendices[10:21]}\n")
