

var divTotal = document.getElementById('comprar__total')
const total = document.getElementById('total')
const contador1 = document.getElementById("contador1");
const contador2 = document.getElementById("contador2");
var count1 = 1;
var count2 = 1;

const precioLPy = 70000
const precioLJs = 85000

function aumento1(){
    count1 += 1;
    contador1.innerHTML = `<span>Cantidad:</span> ${count1}`;
}

function decremento1(){
    count1 <= 1 ? count1 = 1 : count1 -= 1;
    contador1.innerHTML = `<span>Cantidad:</span>  ${count1}`;
}

function aumento2(){
    count2 += 1;
    contador2.innerHTML = `<span>Cantidad:</span>  ${count2}`;
}

function decremento2(){
    count2 <= 1 ? count2 = 1 : count2 -= 1;
    contador2.innerHTML = `<span>Cantidad:</span>  ${count2}`;
}

function comprar(){
    let precioTotal  = (precioLPy * count1) + (precioLJs * count2)
    
    divTotal.style.display = "block"
    total.innerHTML = `El total es de: $${precioTotal}`
}