
function calcularAreas() {

    var opciones = parseInt(prompt("Bienvenido, digite una opción para continuar:\n1. Calcular el area de un cuadrado\n2. Calcular el area de un triangulo\n3. Calcular el area de un rectangulo\n9.Salir"))

    switch (opciones) {
        case 1:
            var lado = parseFloat(prompt("Escriba la longitud que tiene un lado de su cuadrado"))

            var areaCuadrado = lado * lado

            document.write(`El area de su cuadrado es ${areaCuadrado}`)

            break;
        case 2:
            var base = parseFloat(prompt("Escriba la longitud que tiene la base de su triangulo"))
            var altura = parseFloat(prompt("Escriba la longitud que tiene la altura de su triangulo"))

            var areaTriangulo = (base * altura) / 2

            document.write(`El area de su triangulo es ${areaTriangulo}`)

            break;
        case 3:
            var largo = parseFloat(prompt("Escriba la longitud que el largo de su rectangulo"))
            var ancho = parseFloat(prompt("Escriba la longitud que el ancho de su rectangulo"))

            var areaRectangulo = largo * ancho

            document.write(`El area de su rectangulo es ${areaRectangulo}`)

            break;
            
        case 9:
            alert("Gracias por usar este programa :D")
            break;

        default:
            alert("esta opción no existe")
            break;
        }
}


