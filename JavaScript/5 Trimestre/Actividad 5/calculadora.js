

function agregarValor(valor) {
    let operacionContenedor = document.getElementById("operacion");
    operacionContenedor.textContent += `${valor}`; 
}

function calcular(){
    let operacionContenedor = document.getElementById("operacion")
    let operacion = document.getElementById("operacion").textContent;

    operacion = operacion.replace(/÷/g, '/'); 
    operacion = operacion.replace(/×/g, '*'); 
    
    // if(){

    // }
    
    try{
        let resultado = eval(operacion);
        operacionContenedor.textContent = `${resultado}`
    }
    catch(error){
        operacionContenedor.textContent = `Syntax ERROR`
    }

}

function borrar(){
    let operacionContenedor = document.getElementById("operacion")
    let operacion = document.getElementById("operacion").textContent;

    let nuevaOperacion = operacion.substring(0, operacion.length - 1);
    operacionContenedor.textContent = `${nuevaOperacion}`
}

function borrarTodo(){
    let operacionContenedor = document.getElementById("operacion")
    
    operacionContenedor.textContent = '' 
}