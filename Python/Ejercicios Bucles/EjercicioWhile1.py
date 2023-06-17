
#*Digite un número, si el numero supera a 10, multiplique los 10 primeros números, sino, súmelos.

n = int(input("Digite un numero: "))
acum1 = 1
acum2 = 0
count = 1

while count < 10:
    if n > 10:
        acum1 *= count
    else:
        acum2 += count

    count += 1

if n > 10:
    print(acum1)
else:
    print(acum2)


