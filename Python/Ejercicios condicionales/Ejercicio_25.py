
"""
25. Escriba un programa que permita adivinar un personaje de Marvel en base
a las tres preguntas siguientes:
a. ¿Puede volar?
b. ¿Es humano?
c. ¿Tiene máscara?

"""

print("I will guess a superhero :D, so...")

q1 = str(input("can he fly?: "))
q2 = str(input("is he human?: "))
q3 = str(input("has a mask ?: "))

if q1 == "YES" or q1 == "yes" and q2 == "YES" or q2 == "yes" and q3 == "YES" or q3 == "yes":
    print("¡Your superhero is Iroman!")
else:
    print("Oh, I dont know who is he/she :c")
