
"""
Escriba un programa en Python que acepte la opción de dos jugadoras en
a. Piedra-Papel-Tijera y decida el resultado (solución).
b. Entrada: persona1=piedra; persona2=papel
c. Salida: Gana persona2: El papel envuelve a la piedra
"""
menu = 0

while menu == 0:

    print("\nRock, paper and scissors")
    print("\nEnter 1 for \"rock\", 2 for \"paper\", and 3 for \"scissors\"")

    p1 = int(input("\nPlayer 1, write your choice: "))
    p2 = int(input("\nPlayer 2, write your choice: "))

    if p1 == 1 and p2 == 2:
        print("\n¡Player 2 is the winner!")
    elif p1 == 2 and p2 == 3:
        print("\n¡Player 2 is the winner!")
    elif p1 == 3 and p2 ==1:
        print("\n¡Player 2 is the winner!")
    elif p1 == p2 or p2 == p1:
        print("\n¡is a tie!")
    elif p1 and p2 != 1 and p1 and p2 != 2 and p1 and p2 != 3:
        print("\nEnter a valid choice")
    else:
        print("\n¡Player 1 is the winner!")
    
    Exit = str(input("\nDo you want to get out of the game?: "))

    if Exit == "yes" or Exit == "YES":
        break

    



