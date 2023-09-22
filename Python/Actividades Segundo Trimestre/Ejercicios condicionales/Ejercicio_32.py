
"""
La oficina de incorporación del ejercito necesita un algoritmo que le
pueda permitir
saber si un aspirante a ingresar a la institución como soldado es apto o no para
poder vincularlo. Para que una persona sea apta, debe cumplir los siguientes
requisitos:
a. Si es mujer, su estatura debe ser superior a 1.60 más y su edad debe
estar entre 20 y 25 años.
b. Si el aspirante es hombre, se estatura debe ser superior a 1.65 más y
su edad debe estar entre los 18 y 24 años.
c. Tanto mujeres como hombres deben ser solteros.
Diseñe el algoritmo de tal forma que permita informar si un aspirante es apto o no
para ingresar al ejército.

"""

gender = str(input("Enter your gender: "))
height = float(input("Enter your heigth: "))
age = float(input("Enter your age: "))
maritalStatus = str(input("Enter your marital status: "))

if gender == "woman" or gender =="WOMAN":
    if height > 1.60 and age >= 20 and age <= 25 and maritalStatus == "Single" or maritalStatus == "single": 
        print("you are fit to be in the army")
    else:
        print("you are not fit to be in the army")
elif gender == "man" or gender == "MAN":
    if height > 1.65 and age >= 18 and age <= 24 and maritalStatus == "Single" or maritalStatus == "single": 
        print("you are fit to be in the army")
    else:
        print("you are not fit to be in the army")
else:
    print("Enter a valid gender")