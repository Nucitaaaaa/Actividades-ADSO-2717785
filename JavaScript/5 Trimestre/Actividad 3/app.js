
let caracteres = []

function generarContrasena() {
    let letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    let numeros = [1,2,3,4,5,6,7,8,9,0]
    let carEsp = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=',
    '[', ']', '{', '}', '|', ';', ':', ',', '.', '<', '>', '?']
    let contraseña = ''

    let contraseñaDiv = document.getElementById("contraseña")
    let longitud = parseInt(document.getElementById("longitud").value)
    let letrasCheck =  document.getElementById("letras")
    let numerosCheck =  document.getElementById("numeros")
    let carEspCheck =  document.getElementById("carEsp")

    // let randomInd = Math.floor(Math.random() * (caracteres.length));
        
    if (letrasCheck.checked) {
        caracteres.push(...letras)
    }

    if (numerosCheck.checked) {
        caracteres.push(...numeros)
    }

    if (carEspCheck.checked) {
        caracteres.push(...carEsp)
    }

    while(contraseña.length < longitud){
        
    }
}