
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

if q1.upper() == "YES" and q2.upper() == "YES" and q3.upper() == "YES":
    print("¡Your superhero is Iroman!")
elif q1.upper() == "YES" and q2.upper() == "YES" and q3.upper() == "NO":
    print("¡Your superhero is Captain Marvel!")
elif q1.upper() == "YES" and q2.upper() == "NO" and q3.upper() == "NO":
    print("¡Your superhero is Thor!")
else:
    print("Oh, I dont know who is he/she :c")






