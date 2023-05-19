
"""
Un hombre desea saber cuánto dinero se genera por concepto de intereses
en relación la cantidad que tiene en inversión en el banco.
El decidirá reinvertir los intereses siempre y cuando estos no excedan a $7000,
y en ese caso diseña un algoritmo para saber cuánto dinero tendrá
finalmente en su cuenta.
"""

investment = float(input("Enter your initial investment: "))
interest = float(input("Enter the interest rate: "))

reinvestment = investment * interest

if investment <= 7000:
    finalInvestment = investment + reinvestment
    print(f"The final amount of money in your account is {finalInvestment}")

else:
    finalInvestment = investment + 7000
    print(f"The final amount of money in your account is {finalInvestment}")