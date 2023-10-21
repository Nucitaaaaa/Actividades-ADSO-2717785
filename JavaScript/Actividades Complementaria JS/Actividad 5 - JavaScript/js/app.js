
//Funcion para calcular el precio de los platos 
function calcularPrecio() {
    
    //*Seleccion de elementos html para manipular 
    //Seleccion de los valores de los select e input
    var precioComida = parseInt(document.getElementById("selectPlato").value)
    var cantidadComida = parseInt(document.getElementById("cantidadPLato").value)
    var precioBebida = parseInt(document.getElementById("selectBebida").value)
    var cantidadBebida = parseInt(document.getElementById("cantidadBebida").value)
    var precioPostre = parseInt(document.getElementById("selectPostre").value)
    var cantidadPostre = parseInt(document.getElementById("cantidadPostre").value)
    
    //Seleccion del texto de la opción seleccionada de los select 
    var comida = document.getElementById("selectPlato");
    var comidaS = comida.options[comida.selectedIndex].text;
    var bebida = document.getElementById("selectBebida");
    var bebidaS = bebida.options[bebida.selectedIndex].text;
    var postre = document.getElementById("selectPostre");
    var postreS = postre.options[postre.selectedIndex].text;
    
    //Seleccion del div del pedido calculado
    var precioTotal = document.getElementById("pedidoCalculado")

    //*Operaciones para calcular los precios
    //Operación precio total 
    var total = (precioComida * cantidadComida) + (precioBebida * cantidadBebida) + (precioPostre * cantidadPostre);
    //Operaciones precio total de la comida, bebida y postre por separado  
    var totalComida = precioComida * cantidadComida;
    var totalBebida = precioBebida * cantidadBebida;
    var totalPostre = precioPostre * cantidadPostre;

    //*Modificación del div para mostrar los resultados correspondientes
    //cambio del display de none a block para que el div sea visible
    precioTotal.style.display = "block"
    //alteración del contenido del div para mostrar el total del pedido y sus respectivos precios por separado
    precioTotal.innerHTML = `El precio <strong>total</strong> de su pedido es: $${total} <br> <strong>Plato:</strong> ${comidaS} (${cantidadComida})  <strong>Precio:</strong> $${totalComida} <br> <strong>Bebida:</strong> ${bebidaS} (${cantidadBebida})  <strong>Precio:</strong> $${totalBebida} <br> <strong>Postre:</strong> ${postreS} (${cantidadPostre})  <strong>Precio:</strong> $${totalPostre}`
}

//!Funciones agregadas por mi

//Funcion para mostrar el menu con los precios
function mostrarMenu() {
    //Selección de los elementos de html para manipular
    var mostrar = document.getElementById("mostrar")
    var ocultar = document.getElementById("ocultar")
    var menu = document.getElementById("menuComida")

    //Cambio de display de los elementos seleccionados (se oculta el boton de mostrar y se muestra el boton ocultar y el menu)
    menu.style.display = "block"
    ocultar.style.display = "block"
    mostrar.style.display = "none"
}

//Funcion para ocultar el menu con los precios
function ocultarMenu() {
    //Selección de los elementos de html para manipular 
    var mostrar = document.getElementById("mostrar")
    var ocultar = document.getElementById("ocultar")
    var menu = document.getElementById("menuComida")
    
    //Cambio de display de los elementos seleccionados (se oculta el menu y el boton ocultar y se muestra el boton mostrar)
    menu.style.display = "none"
    ocultar.style.display = "none"
    mostrar.style.display = "block"
}