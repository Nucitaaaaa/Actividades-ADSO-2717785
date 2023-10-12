
function suma(n1,n2) {
    var resultado = n1 + n2;
    var res = document.getElementById("resultado");
    //var respuesta = document.getElementById("resultado");

    if(n1 && n2 != 0){
        respuesta.style.display="block";
        res.innerHTML = `Resultado: ${resultado}`;
    }else {
        respuesta.style.display="block";
        res.innerHTML = `No valido`;
    }
}

function resta(n1,n2) {
    var resultado = n1 - n2;
    var res = document.getElementById("resultado");

    if(n1 && n2 != 0){
        respuesta.style.display="block";
        res.innerHTML = `Resultado: ${resultado}`;
    }else {
        respuesta.style.display="block";
        res.innerHTML = `No valido`;
    }
}

function multiplicacion(n1,n2) {
    var resultado = n1 * n2;
    var res = document.getElementById("resultado");

    if(n1 && n2 != 0){
        respuesta.style.display="block";
        res.innerHTML = `Resultado: ${resultado}`;
    }else {
        respuesta.style.display="block";
        res.innerHTML = `No valido`;
    }
}

function division(n1,n2) {
    var resultado = n1 / n2;
    var res = document.getElementById("resultado");

    if(n1 && n2 != 0){
        respuesta.style.display="block";
        res.innerHTML = `Resultado: ${resultado}`;
    }else {
        respuesta.style.display="block";
        res.innerHTML = `No valido`;
    }
}

function potencia(n1) {
    var resultado = n1*n1;
    var res = document.getElementById("resultado");

    if(n1 != 0){
        respuesta.style.display="block";
        res.innerHTML = `Resultado: ${resultado}`;
    }else {
        respuesta.style.display="block";
        res.innerHTML = `No valido`;
    }
}

function mostrar() {
    let n1 = parseInt(document.getElementById("n1").value)
    let n2 = parseInt(document.getElementById("n2").value)
    let opc = parseInt(document.getElementById("opc").value)

    switch(opc) {
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
            alert("No valido")
    }
}