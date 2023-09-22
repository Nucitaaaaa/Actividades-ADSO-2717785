

function calcularAreas() { //Se crea la función para ser utilizada cada vez que se pulse el botón ubicado en el HTML.

    var opciones = parseInt(prompt("Bienvenido, digite una opción para continuar:\n1. Calcular el area de un cuadrado\n2. Calcular el area de un triangulo\n3. Calcular el area de un rectangulo\n9.Salir")) //Se crea la variable menu, para guardar la elección del usuario y en base a esta ejecutar el switch. 

    switch (opciones) { //Se establece la condicion o variable sobre la que va a actuar el switch y se describe que se hará en cada caso segun la decisión del usuario.
        case 1: //el bloque de codigo que se ejecutará en caso de que el usuario digite 1 en la variable opciones.
            var lado = parseFloat(prompt("Escriba la longitud que tiene un lado de su cuadrado"))

            var areaCuadrado = lado * lado

            document.write(`El area de su cuadrado es ${areaCuadrado}`)

            break;
        case 2: //el bloque de codigo que se ejecutará en caso de que el usuario digite 2 en la variable opciones.
            var base = parseFloat(prompt("Escriba la longitud que tiene la base de su triangulo"))
            var altura = parseFloat(prompt("Escriba la longitud que tiene la altura de su triangulo"))

            var areaTriangulo = (base * altura) / 2

            document.write(`El area de su triangulo es ${areaTriangulo}`)

            break;
        case 3: //el bloque de codigo que se ejecutará en caso de que el usuario digite 3 en la variable opciones.
            var largo = parseFloat(prompt("Escriba la longitud que el largo de su rectangulo"))
            var ancho = parseFloat(prompt("Escriba la longitud que el ancho de su rectangulo"))

            var areaRectangulo = largo * ancho

            document.write(`El area de su rectangulo es ${areaRectangulo}`)

            break;
            
        case 9: //el bloque de codigo que se ejecutará en caso de que el usuario digite 9 en la variable opciones.
            alert("Gracias por usar este programa :D")
            break;

        default: //el bloque de codigo que se ejecutará si no se cumple ninguna de las condiciones anteriores.
            alert("esta opción no existe")
            break;
        }
}


