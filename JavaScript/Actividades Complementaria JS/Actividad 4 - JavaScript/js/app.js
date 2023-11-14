
//Se declaran las funciones 

//Función suma 
function suma(n1,n2) {
    // se calcula la suma de los dos numeros 
    var resultado = n1 + n2; 
    var res = document.getElementById("resultado"); // Se obtiene el elemento HTML donde se mostrará el resultado

    if(n1 && n2 != 0){ // Se verifica que ambos números no sean 0

        // Se muestra el resultado y se cambia el estilo del elemento a bloque
        respuesta.style.display="block"; 
        res.innerHTML = `Resultado: ${resultado}`; 

    } else{ // Si alguno de los números es 0, se muestra "No valido"
        respuesta.style.display="block"; 
        res.innerHTML = `No valido`; 
    }
}

// Función resta
function resta(n1, n2) {
    // Se calcula la resta de los dos números
    var resultado = n1 - n2;
    
    // Se obtiene el elemento HTML donde se mostrará el resultado
    var res = document.getElementById("resultado");

    // Se verifica que ambos números no sean 0
    if (n1 && n2 != 0) {
        // Se muestra el resultado y se cambia el estilo del elemento a bloque
        respuesta.style.display = "block";
        res.innerHTML = `Resultado: ${resultado}`;
    } else {
        // Si alguno de los números es 0, se muestra "No valido"
        respuesta.style.display = "block";
        res.innerHTML = `No valido`;
    }
}

// Función multiplicacion
function multiplicacion(n1, n2) {
    // Se calcula la multiplicación de los dos números
    var resultado = n1 * n2;
    var res = document.getElementById("resultado");

    // Se verifica que ambos números no sean 0
    if (n1 && n2 != 0) {
        // Se muestra el resultado y se cambia el estilo del elemento a bloque
        respuesta.style.display = "block";
        res.innerHTML = `Resultado: ${resultado}`;
    } else {
        // Si alguno de los números es 0, se muestra "No valido"
        respuesta.style.display = "block";
        res.innerHTML = `No valido`;
    }
}

// Función division
function division(n1, n2) {
    // Se calcula la división de los dos números
    var resultado = n1 / n2;
    var res = document.getElementById("resultado");

    // Se verifica que ambos números no sean 0
    if (n1 && n2 != 0) {
        // Se muestra el resultado y se cambia el estilo del elemento a bloque
        respuesta.style.display = "block";
        res.innerHTML = `Resultado: ${resultado}`;
    } else {
        // Si alguno de los números es 0, se muestra "No valido"
        respuesta.style.display = "block";
        res.innerHTML = `No valido`;
    }
}

// Función potencia
function potencia(n1) {
    // Se calcula el cuadrado del número
    var resultado = n1 * n1;
    var res = document.getElementById("resultado");

    // Se verifica que el número no sea 0
    if (n1 != 0) {
        // Se muestra el resultado y se cambia el estilo del elemento a bloque
        respuesta.style.display = "block";
        res.innerHTML = `Resultado: ${resultado}`;
    } else {
        // Si el número es 0, se muestra "No valido"
        respuesta.style.display = "block";
        res.innerHTML = `No valido`;
    }
}

//Funcion para mostrar el resultado 
function mostrar() { //se crea la función mostrar y se le asignan dos variables que contienen los numeros y una para la opción 
    let n1 = parseInt(document.getElementById("n1").value)
    let n2 = parseInt(document.getElementById("n2").value)
    let opc = parseInt(document.getElementById("opc").value)

    switch(opc) { //se valida la opció que elegio el usuario y se llama a una u otra función dependiendo de esta
        case 1:
            suma(n1,n2)
            break; 
        case 2:
            resta(n1,n2)
            break;
        case 3:
            multiplicacion(n1,n2)
            break;
        case 4:
            division(n1,n2)
            break;
        case 5:
            potencia(n1)
            break;
        default:
            alert("No valido") //en caso de que se elija una opción no valida
    }
}