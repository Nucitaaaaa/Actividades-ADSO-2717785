
var count = 0;

const contador = document.getElementById("contador");
const precioLpy = 70.000
const precioLJs = 85.000

function aumento(){
    count += 1;
    contador.innerHTML = count;
}

function decremento(){
    count <= 0 ? count = 0 : count -= 1;
    contador.innerHTML = count;
}

function comprar(){
    let totalJs = 
}