
var count = 0

function reiniciar(){
    let contador = document.getElementById("contador")
    
    count = 0
    contador.innerText = `${count}`
}

function aumentar(){
    let contador = document.getElementById("contador")

    count = count += 1

    console.log(count)
    contador.innerText = `${count}`
}

function disminuir(){
    let contador = document.getElementById("contador")

    if (count == 0){
        count = 0
        contador.innerText = `${count}`
    }
    else {
        count = count -= 1
        contador.innerText = `${count}`
    }

    console.log(count)
}