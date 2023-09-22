
"""
Determinar si un aprendiz aprueba o reprueba una formación, sabiendo que
aprobara si su promedio de tres calificaciones es mayor o igual a 10;
reprueba en caso contrario
"""

note1 = float(input("Enter your first note: "))
note2 = float(input("Enter your second note: "))
note3 = float(input("Enter your third note: "))

average = (note1 + note2 + note3) / 3

if average >= 10:
    print("You have passed the course")
else:
    print("You have failed the course")

