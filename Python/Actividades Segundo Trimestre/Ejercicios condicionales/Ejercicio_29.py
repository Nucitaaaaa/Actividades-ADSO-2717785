
"""
Se debe validar tres atajos de visual estudio code si cumple los tres, deberá
informar al usuario que felicidades es correcto de lo contrario debe indicar
que no aplica
"""
print("Enter the following 3 shortcuts:\n\n1-word wrap\n2-close the sidebar\n3-create a new file")
sc1 = str(input("\nEnter the first shortcut here: "))
sc2 = str(input("Enter the second shortcut here: "))
sc3 = str(input("Enter the third shortcut here: "))

if sc1 == "alt + z" or sc1 == "Alt + Z" and sc2 == "ctrl + b" or sc2 == "Ctrl + B" and sc3 == "ctrl + n" or sc3 == "Ctrl + N":
    print("Congratulations, your answers are correct")
else:
    print("Sorry, some of your answers are wrong...")