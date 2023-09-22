
"""
Diseñe un algoritmo que guarde el nombre del aprendiz, nombre del curso,
nota definitiva, el nro de clases en el semestre y el número de las fallas. En el
caso de que las fallas superen el 30% del número de clases se debe mostrar
la nota que no aprobó y se calificara cero(0)
"""

name = str(input("Enter your name: "))
course = str(input("Enter your course name: "))
finalGrade = float(input("Enter your final grade: "))
classes = float(input("Enter the number of classes: "))
absences = float(input("Enter the number of absences to class: "))

notApproved = absences > (classes * 0.3) 

if notApproved is True:
    finalGrade = 0
    print(f"You have failed the course, your final grade is {finalGrade}")
else:
    print(f"You have Passed the course, your final grade is {finalGrade}")



