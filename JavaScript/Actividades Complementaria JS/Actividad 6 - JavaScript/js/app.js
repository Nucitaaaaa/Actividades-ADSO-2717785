
var count = 0;
const contador = document.getElementById("contador");

function aumento(){
    count += 1;
    contador.innerHTML = count;
}

function decremento(){
    count <= 0 ? count = 0 : count -= 1;
    contador.innerHTML = count;
}

function refrescar(){
    count = 0;
    contador.innerHTML = count;
}