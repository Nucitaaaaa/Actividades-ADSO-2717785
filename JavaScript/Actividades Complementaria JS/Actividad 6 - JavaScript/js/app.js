
//Declaracion de variables y constantes
var count = 0; //contador
const contador = document.getElementById("contador"); //div contador

//Funcion aumento del contador (aumenta en 1)
function aumento(){
    count += 1;
    contador.innerHTML = count;
}

//Funcion decremento del contador (disminuye en 1)
function decremento(){
    count <= 0 ? count = 0 : count -= 1;
    contador.innerHTML = count;
}

//Funcion reiniciar contador (vuelve a 0)
function refrescar(){
    count = 0;
    contador.innerHTML = count;
}