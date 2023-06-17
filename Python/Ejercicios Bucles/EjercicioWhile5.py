
#*Crear un programa que permita al usuario ingresar los valores totales de n facturas (se desconoce la cantidad de datos que cargará, la cual puede cambiar en cada ejecución), cortando el ingreso de datos cuando el usuario ingrese el monto 0. Al finalizar, informar el total a pagar teniendo que cuenta que, si las ventas superan el total de $1000, se le debe aplicar un 10% de descuento.

end = 0
total = 0

while not end:
    fact = float(input("Digite el valor de su factura: "))
    total += fact
    if fact == end:
        if total > 1000:
            desc = total * 0.10
            newTotal = total - desc
            print(f"Su total a pagar será de {newTotal}")
            break
        else:
            print(f"Su total a pagar será de {total}")
            break 
