
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
elif q1 == "YES" or q1 == "yes" and q2 == "YES" or q2 == "yes" and q3 == "NO" or q3 == "NO":
    print("¡Your superhero is Captain Marvel!")
elif q1 == "YES" or q1 == "yes" and q2 == "NO" or q2 == "no" and q3 == "NO" or q1 == "no":
    print("¡Your superhero is Thor!")
else:
    print("Oh, I dont know who is he/she :c")






