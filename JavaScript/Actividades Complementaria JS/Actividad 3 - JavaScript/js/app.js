
function calculadora() { //Se crea la función para ser utilizada cada vez que se pulse el botón ubicado en el HTML.


    var opciones = parseInt(prompt("Bienvenido, digite una opción para continuar:\n1. Suma\n2. Resta\n3. Multiplicación\n4. División\n5. Numero mayor\n 9. Salir")) //Se crea la variable menu, para guardar la elección del usuario y en base a esta ejecutar el switch. 

    switch (opciones) { //Se establece la condicion o variable sobre la que va a actuar el switch y se describe que se hará en cada caso segun la decisión del usuario.
        case 1: //el bloque de codigo que se ejecutará en caso de que el usuario digite 1 en la variable opciones.
            var num1 = parseFloat(prompt("Escriba el primer numero: "))
            var num2 = parseFloat(prompt("Escriba el segundo numero: "))

            var suma = num1 + num2

            document.write(`La suma de los dos numeros es ${suma}`)

            break;

        case 2: //el bloque de codigo que se ejecutará en caso de que el usuario digite 2 en la variable opciones.
            var num1 = parseFloat(prompt("Escriba el primer numero: "))
            var num2 = parseFloat(prompt("Escriba el segundo numero: "))

            var resta = num1 - num2

            document.write(`La resta de los dos numeros es ${resta}`)
        
            break;

        case 3: //el bloque de codigo que se ejecutará en caso de que el usuario digite 3 en la variable opciones.
            var num1 = parseFloat(prompt("Escriba el primer numero: "))
            var num2 = parseFloat(prompt("Escriba el segundo numero: "))

            var mul = num1 * num2

            document.write(`La multiplicación de los dos numeros es ${mul}`)

            break;

        case 4: //el bloque de codigo que se ejecutará en caso de que el usuario digite 4 en la variable opciones.
            var num1 = parseFloat(prompt("Escriba el primer numero: "))
            var num2 = parseFloat(prompt("Escriba el segundo numero: "))

            var div = num1 / num2

            document.write(`La división de los dos numeros es ${div}`)

            break;

        case 5: //el bloque de codigo que se ejecutará en caso de que el usuario digite 5 en la variable opciones.
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

        case 9: //el bloque de codigo que se ejecutará en caso de que el usuario digite 9 en la variable opciones.
            break;

        default: //el bloque de codigo que se ejecutará si no se cumple ninguna de las condiciones anteriores.
            alert("esta opción no existe")
            break
        }
}

