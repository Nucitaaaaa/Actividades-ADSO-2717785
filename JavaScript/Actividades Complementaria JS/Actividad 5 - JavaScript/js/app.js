
function calcularPrecio() {
    
    var precioComida = parseInt(document.getElementById("selectPlato").value)
    var cantidadComida = parseInt(document.getElementById("cantidadPLato").value)
    var precioBebida = parseInt(document.getElementById("selectBebida").value)
    var cantidadBebida = parseInt(document.getElementById("cantidadBebida").value)
    var precioPostre = parseInt(document.getElementById("selectPostre").value)
    var cantidadPostre = parseInt(document.getElementById("cantidadPostre").value)

    var comida = document.getElementById("selectPlato");
    var comidaS = comida.options[comida.selectedIndex].text;
    var bebida = document.getElementById("selectBebida");
    var bebidaS = bebida.options[bebida.selectedIndex].text;
    var postre = document.getElementById("selectPostre");
    var postreS = postre.options[postre.selectedIndex].text;
    
    var precioTotal = document.getElementById("pedidoCalculado")

    var total = (precioComida * cantidadComida) + (precioBebida * cantidadBebida) + (precioPostre * cantidadPostre);
    var totalComida = precioComida * cantidadComida;
    var totalBebida = precioBebida * cantidadBebida;
    var totalPostre = precioPostre * cantidadPostre;

    precioTotal.style.display = "block"
    precioTotal.innerHTML = `El precio <strong>total</strong> de su pedido es: $${total} <br> <strong>Plato:</strong> ${comidaS}(x${cantidadComida}) <strong>Precio:</strong> $${totalComida} <br> <strong>Bebida:</strong> ${bebidaS}(x${cantidadBebida}) <strong>Precio:</strong> $${totalBebida} <br> <strong>Postre:</strong> ${postreS}(x${cantidadPostre}) <strong>Precio:</strong> $${totalPostre}`
}

function mostrarMenu() {
    var mostrar = document.getElementById("mostrar")
    var ocultar = document.getElementById("ocultar")

    var menu = document.getElementById("menuComida")
    menu.style.display = "block"
    ocultar.style.display = "block"
    mostrar.style.display = "none"
}

function ocultarMenu() {
    var mostrar = document.getElementById("mostrar")
    var ocultar = document.getElementById("ocultar")

    var menu = document.getElementById("menuComida")
    menu.style.display = "none"
    ocultar.style.display = "none"
    mostrar.style.display = "block"
}