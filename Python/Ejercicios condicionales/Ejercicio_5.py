<<<<<<< HEAD
"""
Un hombre desea saber cuánto dinero se genera por concepto de intereses
en relación la cantidad que tiene en inversión en el banco

=======

"""
Un hombre desea saber cuánto dinero se genera por concepto de intereses
en relación la cantidad que tiene en inversión en el banco.
>>>>>>> 0d627d0f1410373118337e5458cd5267e1e2b45b
El decidirá reinvertir los intereses siempre y cuando estos no excedan a $7000,
y en ese caso diseña un algoritmo para saber cuánto dinero tendrá
finalmente en su cuenta.
"""

<<<<<<< HEAD
investment  = float(input("enter your initial investment: "))
interest = float(input("enter the interest rate: "))
=======
investment = float(input("Enter your initial investment: "))
interest = float(input("Enter the interest rate: "))
>>>>>>> 0d627d0f1410373118337e5458cd5267e1e2b45b

reinvestment = investment * interest

if investment <= 7000:
    finalInvestment = investment + reinvestment
<<<<<<< HEAD
    print(f"the final amount of money in your account is {finalInvestment}")

else:
    finalInvestment = investment + 7000
    print(f"the final amount of money in your account is {finalInvestment}")



=======
    print(f"The final amount of money in your account is {finalInvestment}")

else:
    finalInvestment = investment + 7000
    print(f"The final amount of money in your account is {finalInvestment}")
>>>>>>> 0d627d0f1410373118337e5458cd5267e1e2b45b
