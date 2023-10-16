
function calcularPrecio() {
    
    var precioComida = parseInt(document.getElementById("selectPlato").value)
    var cantidadComida = parseInt(document.getElementById("cantidadPLato").value)
    var precioBebida = parseInt(document.getElementById("selectBebida").value)
    var cantidadBebida = parseInt(document.getElementById("cantidadBebida").value)
    var precioPostre = parseInt(document.getElementById("selectPostre").value)
    var cantidadPostre = parseInt(document.getElementById("cantidadPostre").value)

    var precioTotal = document.getElementById("pedidoCalculado")

    event.preventDefault()

    var total = (precioComida * cantidadComida) + (precioBebida * cantidadBebida) + (precioPostre * cantidadPostre);
    var totalComida = precioComida * cantidadComida;
    var totalBebida = precioBebida * cantidadBebida;
    var totalPostre = precioPostre * cantidadPostre;

    precioTotal.innerHTML = `El precio de sus platos es: $${totalComida} \n El precio de sus bebidas es es: $${totalBebida} \n El precio de sus postres es: $${totalPostre} \n El precio total de su pedido es: $${total}`

    
}