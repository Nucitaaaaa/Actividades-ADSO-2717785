
function generarContrasena() {
    let letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    let numeros = [1,2,3,4,5,6,7,8,9,0]
    let carEsp = ['!', '@', '#', '$', '%', '^', '&', '?']
    let contraseña = ""
    let caracteres = []

    
    let contraseñaDiv = document.getElementById("contraseña")
    let longitud = parseInt(document.getElementById("longitud").value)
    let letrasCheck =  document.getElementById("letras")
    let numerosCheck =  document.getElementById("numeros")
    let carEspCheck =  document.getElementById("carEsp")


    if (letrasCheck.checked) {
        caracteres.push(...letras)
    }

    if (numerosCheck.checked) {
        caracteres.push(...numeros)
    }

    if (carEspCheck.checked) {
        caracteres.push(...carEsp)
    }


    if (caracteres.length === 0) {
        contraseñaDiv.innerText = "Debe indicar al menos un tipo de caracteres permitidos";
        return; 
    }

    if (!longitud) {
        contraseñaDiv.innerText = "Debe indicar la cantidad de caracteres deseados";
        return; 
    }

    else if (longitud < 8 || longitud > 16){
        contraseñaDiv.innerText = "La cantidad de caracteres debe ser mayor a 8 y menor a 16";
        return; 
    }


    while (contraseña.length < longitud) {
        let randomChar = Math.floor(Math.random() * (caracteres.length - 1) + 1);
        contraseña += caracteres[randomChar];
    }
    
    contraseñaDiv.innerText = contraseña.length > 0 ? `${contraseña}` : "Error inesperado"; 
    
    caracteres = [] 
}