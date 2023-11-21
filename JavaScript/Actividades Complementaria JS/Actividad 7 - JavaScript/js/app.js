
//Declaración de variables (Traer elementos HTML con el DOM)
var divTotal = document.getElementById('comprar__total') 
const total = document.getElementById('total')
const contador1 = document.getElementById("contador1");
const contador2 = document.getElementById("contador2");

//Variables de js (contadores)
var count1 = 1;
var count2 = 1;

//Precios de los libros
const precioLPy = 70000
const precioLJs = 85000

//Funcion aumento del contador (Python)
function aumento1(){
    count1 += 1;
    contador1.innerHTML = `<span>Cantidad:</span> ${count1}`;
}

//Funcion decremento del contador (Python)
function decremento1(){
    count1 <= 1 ? count1 = 1 : count1 -= 1;
    contador1.innerHTML = `<span>Cantidad:</span>  ${count1}`;
}

//Funcion aumento del contador (JavaScript)
function aumento2(){
    count2 += 1;
    contador2.innerHTML = `<span>Cantidad:</span>  ${count2}`;
}

//Funcion decremento del contador (JavaScript)
function decremento2(){
    count2 <= 1 ? count2 = 1 : count2 -= 1;
    contador2.innerHTML = `<span>Cantidad:</span>  ${count2}`;
}

//Funcion para realizar la compra
function comprar(){
    let precioTotal  = (precioLPy * count1) + (precioLJs * count2) //suma el precio de la cantidad solicitada de ambos libros
    
    divTotal.style.display = "block" //cambia la vista del div de none a block 
    total.innerHTML = `El total es de: $${precioTotal}` //Texto que muestra el total del "Pedido"
}