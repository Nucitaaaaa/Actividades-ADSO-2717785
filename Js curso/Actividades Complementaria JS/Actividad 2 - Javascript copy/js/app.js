
function calculadora() {

    var opciones = parseInt(prompt("Bienvenido, digite una opción para continuar:\n1. Suma\n2. Resta\n3. Multiplicación\n4. División\n5. Numero mayor\n 9. Salir"))

    switch (opciones) {
        case 1:
            var num1 = parseFloat(prompt("Escriba el primer numero: "))
            var num2 = parseFloat(prompt("Escriba el segundo numero: "))

            var suma = num1 + num2

            document.write(`La suma de los dos numeros es ${suma}`)

            break;

        case 2:
            var num1 = parseFloat(prompt("Escriba el primer numero: "))
            var num2 = parseFloat(prompt("Escriba el segundo numero: "))

            var resta = num1 - num2

            document.write(`La resta de los dos numeros es ${resta}`)
        
            break;

        case 3:
            var num1 = parseFloat(prompt("Escriba el primer numero: "))
            var num2 = parseFloat(prompt("Escriba el segundo numero: "))

            var mul = num1 * num2

            document.write(`La multiplicación de los dos numeros es ${mul}`)

            break;

        case 4:
            var num1 = parseFloat(prompt("Escriba el primer numero: "))
            var num2 = parseFloat(prompt("Escriba el segundo numero: "))

            var div = num1 / num2

            document.write(`La división de los dos numeros es ${div}`)

            break;

        case 5:
            var num1 = parseFloat(prompt("Escriba el primer numero: "))
            var num2 = parseFloat(prompt("Escriba el segundo numero: "))

            if (num1>num2) {
                document.write(`El numero mayor es ${num1}`)
            } else if (num2>num1) {
                document.write(`El numero mayor es ${num2}`)
            } else {
                document.write(`los numeros son iguales`)
            }

            break;

        case 9:
            break;

        default:
            alert("esta opción no existe")
            break
        }
}

