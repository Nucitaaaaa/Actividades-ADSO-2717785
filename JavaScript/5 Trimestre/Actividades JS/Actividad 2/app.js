
var contador = 0

function reiniciarContador(){
    let contadorDiv = document.getElementById("contador")
    
    contador = 0
    contadorDiv.innerText = `${contador}`
}

function aumentarContador(){
    let contadorDiv = document.getElementById("contador")

    contador = contador += 1

    contadorDiv.innerText = `${contador}`
}

function disminuirContador(){
    let contadorDiv = document.getElementById("contador")

    if (contador == 0){
        contador = 0
        contadorDiv.innerText = `${contador}`
    }
    else {
        contador = contador -= 1
        contadorDiv.innerText = `${contador}`
    }

}